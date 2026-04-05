from pyspark.sql import SparkSession                            # importa SparkSession para poder leer archivos con Spark
from pyspark.sql import DataFrame                               # importa el tipo DataFrame para indicar claramente qué devuelven las funciones
from pyspark.sql.types import StructType                        # importa StructType para tipar los esquemas que recibirá el lector

from greenhouse_pipeline.config.settings import DATASETS_BRONZE # importa el diccionario que contiene las rutas bronze de todos los datasets
from greenhouse_pipeline.config.schemas import ESQUEMAS         # importa el diccionario que contiene los esquemas de todos los datasets


def obtener_ruta_dataset_bronze(nombre_dataset: str) -> str:                                    # define una función que devuelve la ruta bronze del dataset solicitado
    if nombre_dataset not in DATASETS_BRONZE:                                                   # verifica si el nombre del dataset existe dentro del mapa de rutas bronze
        raise KeyError(f"No existe ruta bronze configurada para el dataset: {nombre_dataset}")  # lanza un error claro si el dataset no está configurado
    return str(DATASETS_BRONZE[nombre_dataset])                                                 # devuelve la ruta convertida a texto para que Spark la use sin problemas


def obtener_esquema_dataset(nombre_dataset: str) -> StructType:                                 # define una función que devuelve el esquema del dataset solicitado
    if nombre_dataset not in ESQUEMAS:                                                          # verifica si el nombre del dataset existe dentro del diccionario general de esquemas
        raise KeyError(f"No existe esquema configurado para el dataset: {nombre_dataset}")      # lanza un error claro si el dataset no tiene esquema declarado
    return ESQUEMAS[nombre_dataset]                                                             # devuelve el esquema correspondiente al dataset pedido


def leer_csv_con_esquema(                                   # define una función especializada en leer archivos CSV aplicando un esquema explícito
    spark: SparkSession,                                    # recibe la sesión activa de Spark que ejecutará la lectura
    ruta_archivo: str,                                      # recibe la ruta del archivo CSV a leer
    esquema: StructType,                                    # recibe el esquema que debe aplicarse al leer el archivo
) -> DataFrame:                                             # indica que la función devolverá un DataFrame de Spark
    df = (                                                  # comienza a construir el DataFrame que resultará de la lectura del CSV
        spark.read                                          # accede al lector de datos de Spark
        .option("header", "true")                           # indica que el archivo CSV tiene una fila de encabezado con nombres de columnas
        .option("sep", ",")                                 # indica que el separador de columnas del CSV es la coma
        .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")   # define el formato esperado para columnas timestamp
        .option("dateFormat", "yyyy-MM-dd")                 # define el formato esperado para columnas date
        .schema(esquema)                                    # aplica el esquema explícito para evitar inferencias automáticas incorrectas
        .csv(ruta_archivo)                                  # lee el archivo CSV ubicado en la ruta indicada
    )                                                       # cierra la construcción del DataFrame leído desde CSV
    return df                                               # devuelve el DataFrame resultante para que el pipeline pueda seguir trabajándolo


def leer_json_con_esquema(                              # define una función especializada en leer archivos JSON aplicando un esquema explícito
    spark: SparkSession,                                # recibe la sesión activa de Spark que ejecutará la lectura
    ruta_archivo: str,                                  # recibe la ruta del archivo JSON a leer
    esquema: StructType,                                # recibe el esquema que debe aplicarse al leer el archivo
) -> DataFrame:                                         # indica que la función devolverá un DataFrame de Spark
    df = (                                              # comienza a construir el DataFrame que resultará de la lectura del JSON
        spark.read                                      # accede al lector de datos de Spark
        .option("multiline", "true")                    # permite leer JSON multilinea o arreglos JSON escritos en varias líneas
        .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")  # define el formato esperado para columnas timestamp dentro del JSON
        .option("dateFormat", "yyyy-MM-dd")             # define el formato esperado para columnas date dentro del JSON
        .schema(esquema)                                # aplica el esquema explícito para controlar tipos y nombres de columnas
        .json(ruta_archivo)                             # lee el archivo JSON ubicado en la ruta indicada
    )                                                   # cierra la construcción del DataFrame leído desde JSON
    return df                                           # devuelve el DataFrame resultante para que el pipeline pueda seguir trabajándolo


def leer_dataset_bronze(                                                    # DEFINE una función general que sabe leer cualquier dataset bronze del proyecto
    spark: SparkSession,                                                    # recibe la sesión activa de Spark que ejecutará la lectura
    nombre_dataset: str,                                                    # recibe el nombre lógico del dataset que se desea leer
) -> DataFrame:                                                             # INDICA que la función devolverá un DataFrame de Spark
    ruta_dataset = obtener_ruta_dataset_bronze(nombre_dataset)              # OBTIENE la ruta bronze correspondiente al dataset pedido
    esquema_dataset = obtener_esquema_dataset(nombre_dataset)               # OBTIENE el esquema que corresponde al dataset pedido

    if nombre_dataset == "weather_api_events":                              # verifica si el dataset solicitado es el de clima externo que viene en formato JSON
        return leer_json_con_esquema(spark, ruta_dataset, esquema_dataset)  # delega la lectura al lector JSON y devuelve el DataFrame resultante

    return leer_csv_con_esquema(spark, ruta_dataset, esquema_dataset)       # para todos los demás datasets usa el lector CSV y devuelve el DataFrame resultante