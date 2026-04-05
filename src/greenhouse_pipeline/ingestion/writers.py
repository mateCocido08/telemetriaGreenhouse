from pathlib import Path

from pyspark.sql import DataFrame

from greenhouse_pipeline.config.settings import DATASETS_SILVER, FORMATO_SALIDA, MODO_ESCRITURA


def obtener_ruta_dataset_silver(nombre_dataset: str) -> str:
    if nombre_dataset not in DATASETS_SILVER:
        raise KeyError(f"No existe ruta silver configurada para el dataset: {nombre_dataset}")
    return str(DATASETS_SILVER[nombre_dataset])


def asegurar_carpeta_padre_salida(ruta_salida: str) -> None:
    Path(ruta_salida).parent.mkdir(parents=True, exist_ok=True)


def escribir_parquet(
    df: DataFrame,
    ruta_salida: str,
    modo_escritura: str,
) -> None:
    asegurar_carpeta_padre_salida(ruta_salida)
    (
        df.write
        .mode(modo_escritura)
        .parquet(ruta_salida)
    )


def escribir_dataset_silver(
    df: DataFrame,
    nombre_dataset: str,
) -> None:
    ruta_salida = obtener_ruta_dataset_silver(nombre_dataset)

    if FORMATO_SALIDA == "parquet":
        escribir_parquet(df, ruta_salida, MODO_ESCRITURA)
        return

    raise ValueError(f"Formato de salida no soportado: {FORMATO_SALIDA}")
