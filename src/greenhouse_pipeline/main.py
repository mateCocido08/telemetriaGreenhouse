from pyspark.sql import SparkSession

from greenhouse_pipeline.config.settings import (
    NOMBRE_PIPELINE,
    SPARK_APP_NAME,
    SPARK_MASTER,
)
from greenhouse_pipeline.ingestion.pipelines import ejecutar_todos_los_pipelines
from greenhouse_pipeline.logging_utils.logger import obtener_logger


def crear_spark_session() -> SparkSession:
    """Crea o recupera la SparkSession usada por el pipeline."""
    return (
        SparkSession.builder
        .appName(SPARK_APP_NAME)
        .master(SPARK_MASTER)
        .getOrCreate()
    )


def main() -> None:
    logger = obtener_logger()
    spark = None

    logger.info("Inicia la aplicación principal del pipeline '%s'", NOMBRE_PIPELINE)

    try:
        spark = crear_spark_session()
        logger.info("SparkSession creada correctamente")

        ejecutar_todos_los_pipelines(spark)
        logger.info("La ejecución completa de todos los pipelines finalizó correctamente")

    except Exception as error:
        logger.error("Ocurrió un error durante la ejecución principal: %s", error)
        raise

    finally:
        if spark is not None:
            spark.stop()
            logger.info("SparkSession detenida correctamente")

        logger.info("Finaliza la aplicación principal del pipeline '%s'", NOMBRE_PIPELINE)


if __name__ == "__main__":
    main()
