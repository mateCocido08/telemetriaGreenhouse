from pyspark.sql import SparkSession                                                        # importa SparkSession para tipar la sesión de Spark que recibirá el orquestador

from greenhouse_pipeline.ingestion.readers import leer_dataset_bronze                       # importa la función general que sabe leer cualquier dataset bronze
from greenhouse_pipeline.ingestion.writers import escribir_dataset_silver                   # importa la función general que sabe escribir cualquier dataset en silver
from greenhouse_pipeline.quality.validators import ejecutar_validaciones_dataset            # importa la función que ejecuta todas las validaciones de calidad de un dataset
from greenhouse_pipeline.logging_utils.logger import obtener_logger                         # importa la función que devuelve el logger configurado del proyecto


logger = obtener_logger()                                                   # CREA o RECUPERA el logger del proyecto para registrar lo que ocurre durante la orquestación


def procesar_dataset_bronze_a_silver(                      # define una función general que procesa un dataset desde bronze hasta silver
    spark: SparkSession,                                                                    # recibe la sesión activa de Spark con la que se leerá y procesará el dataset
    nombre_dataset: str,                                                                    # recibe el nombre lógico del dataset que se desea procesar
) -> None:                                                                                  # indica que la función ejecuta acciones pero no devuelve un valor
    logger.info(f"Inicia el procesamiento del dataset: {nombre_dataset}")                   # registra en logs el comienzo del procesamiento del dataset actual

    df = leer_dataset_bronze(spark, nombre_dataset)             # LEE el dataset desde la capa bronze usando el lector general del proyecto
    cantidad_registros = df.count()                             # CUENTA cuántas filas fueron leídas para tener trazabilidad del volumen procesado
    logger.info(                                                                            # inicia el registro de un mensaje informativo posterior a la lectura
        f"Lectura completada para '{nombre_dataset}' con {cantidad_registros} registros"    # informa el nombre del dataset y la cantidad de filas leídas
    )                                                                                       # cierra la llamada al logger que informa la lectura completada

    ejecutar_validaciones_dataset(df, nombre_dataset)           # EJECUTA todas las validaciones configuradas para el dataset actual
    logger.info(f"Validaciones completadas correctamente para '{nombre_dataset}'")          # registra que el dataset superó las validaciones de calidad

    escribir_dataset_silver(df, nombre_dataset)                 # ESCRIBE el DataFrame validado en la ruta correspondiente de la capa silver
    logger.info(f"Escritura completada en silver para '{nombre_dataset}'")                  # registra que la escritura en silver terminó correctamente

    logger.info(f"Finaliza el procesamiento del dataset: {nombre_dataset}")                 # registra el cierre exitoso del flujo completo del dataset actual


def ejecutar_pipeline_devices_master(spark: SparkSession) -> None:                          # define una función específica para procesar el dataset devices_master
    procesar_dataset_bronze_a_silver(spark, "devices_master")                               # DELEGA el procesamiento completo al orquestador general usando el nombre lógico del dataset


def ejecutar_pipeline_zones_master(spark: SparkSession) -> None:                            # define una función específica para procesar el dataset zones_master
    procesar_dataset_bronze_a_silver(spark, "zones_master")                                 # DELEGA el procesamiento completo al orquestador general usando el nombre lógico del dataset


def ejecutar_pipeline_sensor_events(spark: SparkSession) -> None:                           # define una función específica para procesar el dataset sensor_events
    procesar_dataset_bronze_a_silver(spark, "sensor_events")                                # DELEGA el procesamiento completo al orquestador general usando el nombre lógico del dataset


def ejecutar_pipeline_actuator_events(spark: SparkSession) -> None:                         # define una función específica para procesar el dataset actuator_events
    procesar_dataset_bronze_a_silver(spark, "actuator_events")                              # DELEGA el procesamiento completo al orquestador general usando el nombre lógico del dataset


def ejecutar_pipeline_weather_api_events(spark: SparkSession) -> None:                      # define una función específica para procesar el dataset weather_api_events
    procesar_dataset_bronze_a_silver(spark, "weather_api_events")                           # DELEGA el procesamiento completo al orquestador general usando el nombre lógico del dataset


def ejecutar_todos_los_pipelines(spark: SparkSession) -> None:                              # define una función que ejecuta todos los datasets del proyecto en un orden controlado
    logger.info("Inicia la ejecución completa de todos los pipelines del proyecto")         # registra el comienzo del lote completo de pipelines

    ejecutar_pipeline_devices_master(spark)                                                 # PROCESA primero el catálogo de dispositivos para dejar disponible la dimensión técnica base
    ejecutar_pipeline_zones_master(spark)                                                   # PROCESA luego el catálogo de zonas para dejar disponible la dimensión espacial base
    ejecutar_pipeline_sensor_events(spark)                                                  # PROCESA después los eventos de sensores ya con los maestros cargados
    ejecutar_pipeline_actuator_events(spark)                                                # PROCESA luego los eventos de actuadores
    ejecutar_pipeline_weather_api_events(spark)                                             # PROCESA por último la fuente externa de clima

    logger.info("Finaliza la ejecución completa de todos los pipelines del proyecto")       # registra el cierre del lote completo de pipelines