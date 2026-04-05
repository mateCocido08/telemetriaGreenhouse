from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from greenhouse_pipeline.config.quality_rules import REGLAS_CALIDAD


def obtener_reglas_dataset(nombre_dataset: str) -> dict:
    if nombre_dataset not in REGLAS_CALIDAD:
        raise KeyError(f"No existen reglas de calidad para el dataset: {nombre_dataset}")
    return REGLAS_CALIDAD[nombre_dataset]


def validar_dataset_no_vacio(df: DataFrame, nombre_dataset: str) -> None:
    if df.limit(1).count() == 0:
        raise ValueError(f"El dataset '{nombre_dataset}' está vacío")


def validar_columnas_requeridas(
    df: DataFrame,
    columnas_requeridas: list,
    nombre_dataset: str,
) -> None:
    columnas_faltantes = sorted(set(columnas_requeridas) - set(df.columns))
    if columnas_faltantes:
        raise ValueError(
            f"Al dataset '{nombre_dataset}' le faltan columnas requeridas: {columnas_faltantes}"
        )


def validar_columnas_no_nulas(
    df: DataFrame,
    columnas_no_nulas: list,
    nombre_dataset: str,
) -> None:
    errores_nulos = {}

    for columna in columnas_no_nulas:
        cantidad_nulos = df.filter(col(columna).isNull()).count()
        if cantidad_nulos > 0:
            errores_nulos[columna] = cantidad_nulos

    if errores_nulos:
        raise ValueError(
            f"El dataset '{nombre_dataset}' tiene nulos en columnas obligatorias: {errores_nulos}"
        )


def validar_valores_permitidos(
    df: DataFrame,
    valores_permitidos: dict,
    nombre_dataset: str,
) -> None:
    errores_catalogo = {}

    for columna, valores_validos in valores_permitidos.items():
        if not valores_validos:
            continue

        df_invalidos = df.filter(
            col(columna).isNotNull() & (~col(columna).isin(valores_validos))
        )
        cantidad_invalidos = df_invalidos.count()

        if cantidad_invalidos > 0:
            muestra_valores = [
                fila[columna]
                for fila in df_invalidos.select(columna).distinct().limit(10).collect()
            ]
            errores_catalogo[columna] = {
                "cantidad_invalidos": cantidad_invalidos,
                "muestra_valores": muestra_valores,
            }

    if errores_catalogo:
        raise ValueError(
            f"El dataset '{nombre_dataset}' tiene valores no permitidos: {errores_catalogo}"
        )


def validar_rangos_numericos(
    df: DataFrame,
    rangos_numericos: dict,
    nombre_dataset: str,
) -> None:
    errores_rango = {}

    for columna, regla in rangos_numericos.items():
        if not regla:
            continue

        if columna == "metric_value":
            # En sensor_events, el rango válido depende de la métrica observada.
            for metrica, limites in regla.items():
                cantidad_fuera_rango = df.filter(
                    (col("metric_name") == metrica)
                    & col("metric_value").isNotNull()
                    & (
                        (col("metric_value") < limites["min"])
                        | (col("metric_value") > limites["max"])
                    )
                ).count()

                if cantidad_fuera_rango > 0:
                    errores_rango[metrica] = {
                        "cantidad_fuera_rango": cantidad_fuera_rango,
                        "min": limites["min"],
                        "max": limites["max"],
                    }
        else:
            cantidad_fuera_rango = df.filter(
                col(columna).isNotNull()
                & (
                    (col(columna) < regla["min"])
                    | (col(columna) > regla["max"])
                )
            ).count()

            if cantidad_fuera_rango > 0:
                errores_rango[columna] = {
                    "cantidad_fuera_rango": cantidad_fuera_rango,
                    "min": regla["min"],
                    "max": regla["max"],
                }

    if errores_rango:
        raise ValueError(
            f"El dataset '{nombre_dataset}' tiene valores fuera de rango: {errores_rango}"
        )


def validar_duplicados(
    df: DataFrame,
    columnas_clave: list,
    nombre_dataset: str,
) -> None:
    if not columnas_clave:
        return

    cantidad_grupos_duplicados = (
        df.groupBy(*columnas_clave)
        .count()
        .filter(col("count") > 1)
        .count()
    )

    if cantidad_grupos_duplicados > 0:
        raise ValueError(
            f"El dataset '{nombre_dataset}' tiene duplicados según las columnas clave "
            f"{columnas_clave}. Cantidad de grupos duplicados: {cantidad_grupos_duplicados}"
        )


def ejecutar_validaciones_dataset(df: DataFrame, nombre_dataset: str) -> None:
    reglas = obtener_reglas_dataset(nombre_dataset)

    validar_dataset_no_vacio(df, nombre_dataset)
    validar_columnas_requeridas(df, reglas["columnas_requeridas"], nombre_dataset)
    validar_columnas_no_nulas(df, reglas["columnas_no_nulas"], nombre_dataset)
    validar_valores_permitidos(df, reglas["valores_permitidos"], nombre_dataset)
    validar_rangos_numericos(df, reglas["rangos_numericos"], nombre_dataset)
    validar_duplicados(df, reglas["columnas_clave_duplicados"], nombre_dataset)
