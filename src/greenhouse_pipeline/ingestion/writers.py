from pathlib import Path  # importa Path para trabajar con rutas locales y crear carpetas de salida si hace falta
from pyspark.sql import DataFrame  # importa el tipo DataFrame para indicar claramente qué recibe este archivo

from greenhouse_pipeline.config.settings import DATASETS_SILVER  # importa el diccionario que contiene las rutas silver de todos los datasets
from greenhouse_pipeline.config.settings import MODO_ESCRITURA  # importa el modo general de escritura configurado para el pipeline
from greenhouse_pipeline.config.settings import FORMATO_SALIDA  # importa el formato general de salida configurado para el pipeline


def obtener_ruta_dataset_silver(nombre_dataset: str) -> str:  # define una función que devuelve la ruta silver del dataset solicitado
    if nombre_dataset not in DATASETS_SILVER:  # verifica si el nombre del dataset existe dentro del mapa de rutas silver
        raise KeyError(f"No existe ruta silver configurada para el dataset: {nombre_dataset}")  # lanza un error claro si el dataset no está configurado en la salida
    return str(DATASETS_SILVER[nombre_dataset])  # devuelve la ruta convertida a texto para que Spark pueda escribir allí


def asegurar_carpeta_padre_salida(ruta_salida: str) -> None:  # define una función que asegura la existencia de la carpeta padre de la ruta de salida
    Path(ruta_salida).parent.mkdir(parents=True, exist_ok=True)  # crea las carpetas necesarias por encima de la ruta final y no falla si ya existen


def escribir_parquet(  # define una función especializada en escribir un DataFrame en formato parquet
    df: DataFrame,  # recibe el DataFrame que será escrito en disco
    ruta_salida: str,  # recibe la ruta destino donde se guardará el dataset
    modo_escritura: str,  # recibe el modo de escritura como overwrite o append
) -> None:  # indica que la función realiza una acción pero no devuelve un valor
    asegurar_carpeta_padre_salida(ruta_salida)  # asegura que exista la carpeta padre antes de escribir el dataset
    (  # abre el bloque encadenado de escritura del DataFrame
        df.write  # accede al escritor de DataFrames de Spark
        .mode(modo_escritura)  # aplica el modo de escritura configurado para controlar reemplazo o agregado
        .parquet(ruta_salida)  # escribe el DataFrame en formato parquet en la ruta indicada
    )  # cierra el bloque encadenado de escritura


def escribir_dataset_silver(  # define una función general que sabe escribir cualquier dataset del proyecto en la capa silver
    df: DataFrame,  # recibe el DataFrame ya leído, validado y listo para persistir
    nombre_dataset: str,  # recibe el nombre lógico del dataset que se desea escribir
) -> None:  # indica que la función ejecuta la escritura pero no devuelve un valor
    ruta_salida = obtener_ruta_dataset_silver(nombre_dataset)  # obtiene la ruta silver que corresponde al dataset solicitado

    if FORMATO_SALIDA == "parquet":  # verifica si el formato de salida configurado globalmente es parquet
        escribir_parquet(df, ruta_salida, MODO_ESCRITURA)  # delega la escritura a la función especializada en parquet
        return  # termina la función una vez completada la escritura correcta

    raise ValueError(f"Formato de salida no soportado: {FORMATO_SALIDA}")  # lanza un error si se configuró un formato aún no implementado