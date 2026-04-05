from pyspark.sql import SparkSession

from greenhouse_pipeline.ingestion.readers import leer_dataset_bronze
from greenhouse_pipeline.ingestion.writers import escribir_dataset_silver
from greenhouse_pipeline.logging_utils.logger import obtener_logger
from greenhouse_pipeline.quality.validators import ejecutar_validaciones_dataset

logger = obtener_logger()


def procesar_dataset_bronze_a_silver(
    spark: SparkSession,
    nombre_dataset: str,
) -> None:
    logger.info("Inicia el procesamiento del dataset: %s", nombre_dataset)

    df = leer_dataset_bronze(spark, nombre_dataset)
    cantidad_registros = df.count()
    logger.info(
        "Lectura completada para '%s' con %s registros",
        nombre_dataset,
        cantidad_registros,
    )

    ejecutar_validaciones_dataset(df, nombre_dataset)
    logger.info("Validaciones completadas correctamente para '%s'", nombre_dataset)

    escribir_dataset_silver(df, nombre_dataset)
    logger.info("Escritura completada en silver para '%s'", nombre_dataset)

    logger.info("Finaliza el procesamiento del dataset: %s", nombre_dataset)


def ejecutar_pipeline_devices_master(spark: SparkSession) -> None:
    procesar_dataset_bronze_a_silver(spark, "devices_master")


def ejecutar_pipeline_zones_master(spark: SparkSession) -> None:
    procesar_dataset_bronze_a_silver(spark, "zones_master")


def ejecutar_pipeline_sensor_events(spark: SparkSession) -> None:
    procesar_dataset_bronze_a_silver(spark, "sensor_events")


def ejecutar_pipeline_actuator_events(spark: SparkSession) -> None:
    procesar_dataset_bronze_a_silver(spark, "actuator_events")


def ejecutar_pipeline_weather_api_events(spark: SparkSession) -> None:
    procesar_dataset_bronze_a_silver(spark, "weather_api_events")


def ejecutar_todos_los_pipelines(spark: SparkSession) -> None:
    """
    Ejecuta el lote completo en un orden estable.

    Los datasets maestros se procesan primero para dejar listas las dimensiones
    base del dominio antes de cargar eventos.
    """
    logger.info("Inicia la ejecución completa de todos los pipelines del proyecto")

    ejecutar_pipeline_devices_master(spark)
    ejecutar_pipeline_zones_master(spark)
    ejecutar_pipeline_sensor_events(spark)
    ejecutar_pipeline_actuator_events(spark)
    ejecutar_pipeline_weather_api_events(spark)

    logger.info("Finaliza la ejecución completa de todos los pipelines del proyecto")
