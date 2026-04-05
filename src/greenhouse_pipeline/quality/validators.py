from pyspark.sql import DataFrame       # importa el tipo DataFrame para indicar claramente con qué trabaja este archivo
from pyspark.sql.functions import col   # importa la función col para referirse a columnas de un DataFrame en filtros y expresiones
from greenhouse_pipeline.config.quality_rules import REGLAS_CALIDAD  # importa el diccionario maestro que reúne todas las reglas de calidad por dataset

def obtener_reglas_dataset(nombre_dataset: str) -> dict:  # define una función que devuelve las reglas de calidad del dataset solicitado
    if nombre_dataset not in REGLAS_CALIDAD:    # verifica que el nombre del dataset exista dentro del diccionario general de reglas
        raise KeyError(f"No existen reglas de calidad para el dataset: {nombre_dataset}")  # lanza un error claro si el dataset no fue configurado
    return REGLAS_CALIDAD[nombre_dataset]   # devuelve el bloque de reglas correspondiente al dataset pedido

def validar_dataset_no_vacio(df: DataFrame, nombre_dataset: str) -> None:  # define una función que verifica que el DataFrame tenga al menos una fila
    if df.limit(1).count() == 0:    # toma como máximo una fila y cuenta cuántas encontró para detectar si el dataset está vacío
        raise ValueError(f"El dataset '{nombre_dataset}' está vacío")  # lanza un error si no hay filas para procesar

def validar_columnas_requeridas(df: DataFrame, columnas_requeridas: list, nombre_dataset: str) -> None:  # define una función que controla si existen todas las columnas obligatorias
    columnas_faltantes = sorted(set(columnas_requeridas) - set(df.columns))     # calcula qué columnas esperadas no están presentes en el DataFrame
    if columnas_faltantes:      # verifica si la lista de columnas faltantes tiene contenido
        raise ValueError(f"Al dataset '{nombre_dataset}' le faltan columnas requeridas: {columnas_faltantes}")  # lanza un error indicando exactamente qué columnas faltan

def validar_columnas_no_nulas(df: DataFrame, columnas_no_nulas: list, nombre_dataset: str) -> None:  # define una función que controla qué columnas obligatorias vienen con valores nulos
    errores_nulos = {}      # crea un diccionario vacío para guardar la cantidad de nulos detectados por columna
    for columna in columnas_no_nulas:   # recorre una por una las columnas que no deberían tener nulos
        cantidad_nulos = df.filter(col(columna).isNull()).count()  # filtra las filas donde la columna actual es nula y cuenta cuántas hay
        if cantidad_nulos > 0:      # verifica si encontró al menos un nulo en esa columna
            errores_nulos[columna] = cantidad_nulos  # guarda la columna y la cantidad de nulos detectados
    if errores_nulos:   # verifica si el diccionario de errores tiene contenido
        raise ValueError(f"El dataset '{nombre_dataset}' tiene nulos en columnas obligatorias: {errores_nulos}")  # lanza un error detallando qué columnas tienen nulos y cuántos

def validar_valores_permitidos(df: DataFrame, valores_permitidos: dict, nombre_dataset: str) -> None:  # define una función que valida si ciertas columnas respetan catálogos cerrados de valores
    errores_catalogo = {}   # crea un diccionario vacío para registrar valores inválidos por columna
    for columna, valores_validos in valores_permitidos.items():     # recorre cada columna que tiene un catálogo de valores aceptados
        if not valores_validos:     # verifica si la lista de valores válidos está vacía
            continue    # salta esa columna porque no hay nada para validar
        df_invalidos = df.filter(col(columna).isNotNull() & (~col(columna).isin(valores_validos)))  # filtra las filas donde el valor no es nulo y además no pertenece al catálogo permitido
        cantidad_invalidos = df_invalidos.count()   # cuenta cuántas filas inválidas encontró para esa columna
        if cantidad_invalidos > 0:      # verifica si hubo al menos un valor inválido
            muestra_valores = [fila[columna] for fila in df_invalidos.select(columna).distinct().limit(10).collect()]  # arma una muestra corta de valores incorrectos para facilitar el diagnóstico
            errores_catalogo[columna] = {   # crea una entrada en el diccionario de errores para esa columna
                "cantidad_invalidos": cantidad_invalidos,   # guarda cuántas filas inválidas se detectaron
                "muestra_valores": muestra_valores,     # guarda una pequeña muestra de valores fuera de catálogo
            } 
    if errores_catalogo:  # verifica si se detectó al menos una columna con valores fuera de catálogo
        raise ValueError(f"El dataset '{nombre_dataset}' tiene valores no permitidos: {errores_catalogo}")  # lanza un error detallado con columnas afectadas y ejemplos

def validar_rangos_numericos(df: DataFrame, rangos_numericos: dict, nombre_dataset: str) -> None:  # define una función que valida si ciertos números caen dentro de rangos razonables
    errores_rango = {}  # crea un diccionario vacío para guardar problemas de rango detectados
    for columna, regla in rangos_numericos.items():  # recorre cada columna que tiene asociada una regla de rango
        if not regla:  # verifica si la regla está vacía
            continue  # salta esa columna porque no hay nada que validar
        if columna == "metric_value":  # verifica si la columna actual es metric_value, que usa subrangos según metric_name
            for metrica, limites in regla.items():  # recorre cada métrica y sus límites mínimos y máximos permitidos
                cantidad_fuera_rango = df.filter(  # comienza a construir el filtro para detectar filas fuera de rango
                    (col("metric_name") == metrica) &  # exige que la fila corresponda a la métrica actual
                    col("metric_value").isNotNull() &  # exige que metric_value no sea nulo para validar el rango
                    (  # abre el bloque lógico de comparación de límites
                        (col("metric_value") < limites["min"]) |  # detecta valores menores al mínimo permitido
                        (col("metric_value") > limites["max"])  # detecta valores mayores al máximo permitido
                    )  
                ).count()  # cuenta cuántas filas quedaron fuera del rango permitido
                if cantidad_fuera_rango > 0:  # verifica si hubo al menos una fila fuera de rango para esa métrica
                    errores_rango[metrica] = {  # crea una entrada en el diccionario de errores usando el nombre de la métrica como clave
                        "cantidad_fuera_rango": cantidad_fuera_rango,  # guarda la cantidad de filas fuera de rango
                        "min": limites["min"],  # guarda el mínimo esperado para referencia
                        "max": limites["max"],  # guarda el máximo esperado para referencia
                    } 
        else:  # entra aquí cuando la columna tiene un rango directo y no depende de metric_name
            cantidad_fuera_rango = df.filter(  # comienza a construir el filtro para la columna numérica actual
                col(columna).isNotNull() &  # exige que la columna no sea nula antes de validar el rango
                (  # abre el bloque lógico de comparación de límites
                    (col(columna) < regla["min"]) |  # detecta valores menores al mínimo permitido
                    (col(columna) > regla["max"])  # detecta valores mayores al máximo permitido
                ) 
            ).count()  # cuenta cuántas filas quedaron fuera del rango permitido
            if cantidad_fuera_rango > 0:  # verifica si hubo al menos una fila fuera de rango en esa columna
                errores_rango[columna] = {  # crea una entrada en el diccionario de errores usando el nombre de la columna como clave
                    "cantidad_fuera_rango": cantidad_fuera_rango,  # guarda la cantidad de filas fuera de rango
                    "min": regla["min"],  # guarda el mínimo esperado para referencia
                    "max": regla["max"],  # guarda el máximo esperado para referencia
                }
    if errores_rango:  # verifica si el diccionario de errores de rango contiene información
        raise ValueError(f"El dataset '{nombre_dataset}' tiene valores fuera de rango: {errores_rango}")  # lanza un error detallando qué métricas o columnas quedaron fuera de rango

def validar_duplicados(df: DataFrame, columnas_clave: list, nombre_dataset: str) -> None:  # define una función que detecta registros repetidos según una clave natural
    if not columnas_clave:  # verifica si la lista de columnas clave está vacía
        return  # termina la función porque no hay criterio configurado para buscar duplicados
    cantidad_grupos_duplicados = df.groupBy(*columnas_clave).count().filter(col("count") > 1).count()  # agrupa por la clave natural, cuenta filas por grupo y luego cuenta cuántos grupos tienen más de un registro
    if cantidad_grupos_duplicados > 0:  # verifica si se detectó al menos un grupo duplicado
        raise ValueError(  # comienza a construir el error que se lanzará al encontrar duplicados
            f"El dataset '{nombre_dataset}' tiene duplicados según las columnas clave {columnas_clave}. "  # informa el dataset y la clave usada para detectar repetidos
            f"Cantidad de grupos duplicados: {cantidad_grupos_duplicados}"  # informa cuántos grupos duplicados se detectaron
        )

def ejecutar_validaciones_dataset(df: DataFrame, nombre_dataset: str) -> None:  # define una función orquestadora que ejecuta todas las validaciones para un dataset
    reglas = obtener_reglas_dataset(nombre_dataset)  # obtiene el bloque completo de reglas correspondiente al dataset actual
    validar_dataset_no_vacio(df, nombre_dataset)  # ejecuta la validación que comprueba que el dataset no esté vacío
    validar_columnas_requeridas(df, reglas["columnas_requeridas"], nombre_dataset)  # ejecuta la validación de presencia de columnas obligatorias
    validar_columnas_no_nulas(df, reglas["columnas_no_nulas"], nombre_dataset)  # ejecuta la validación de nulos en columnas críticas
    validar_valores_permitidos(df, reglas["valores_permitidos"], nombre_dataset)  # ejecuta la validación de catálogos de valores aceptados
    validar_rangos_numericos(df, reglas["rangos_numericos"], nombre_dataset)  # ejecuta la validación de rangos numéricos razonables
    validar_duplicados(df, reglas["columnas_clave_duplicados"], nombre_dataset)  # ejecuta la validación de registros duplicados según clave natural