from pyspark.sql import SparkSession                                                # importa SparkSession para poder crear la sesión principal de Spark del proyecto

from greenhouse_pipeline.config.settings import SPARK_APP_NAME                              # importa el nombre escogido para la aplicación Spark
from greenhouse_pipeline.config.settings import SPARK_MASTER                                # importa el modo de ejecución configurado para Spark
from greenhouse_pipeline.config.settings import NOMBRE_PIPELINE                             # importa el nombre general del pipeline para usarlo en mensajes
from greenhouse_pipeline.logging_utils.logger import obtener_logger                         # importa la función obtener_logger(), que devuelve el logger configurado del proyecto
from greenhouse_pipeline.ingestion.pipelines import ejecutar_todos_los_pipelines            # importa la función ejecutar_todos_los_pipelines(), que corre todos los pipelines del proyecto


def crear_spark_session() -> SparkSession:                                                  # DEFINE una función crear_spark_session(), que crea y devuelve la sesión principal de Spark
    spark = (                                                                                   # Comienza la construccion del objeto spark
        SparkSession.builder                                                                        # accede al builder de SparkSession para configurar la sesión
        .appName(SPARK_APP_NAME)                                                                    # ASIGNA el nombre configurado a la aplicación Spark
        .master(SPARK_MASTER)                                                                       # ASIGNA el modo de ejecución configurado, por ejemplo local[*]
        .getOrCreate()                                                                              # CREA la sesión si no existe o recupera una ya existente
    )                                                                                       
    return spark                                                                                # DEVUELVE la sesión Spark lista para ser usada por el resto del proyecto


def main() -> None:                                                                         # DEFINE la función principal que orquesta la ejecución completa del proyecto
    logger = obtener_logger()                               # OBTIENE el logger configurado para registrar el flujo global de la aplicación
    spark = None                                                                                # INICIALIZA la variable spark en None, para poder manejarla de forma segura en el bloque finally

    logger.info(f"Inicia la aplicación principal del pipeline '{NOMBRE_PIPELINE}'")             # REGISTRA que el programa principal comenzó su ejecución

    try:                                                                                        # inicia un bloque de control de errores, para ejecutar el pipeline de forma segura
        spark = crear_spark_session()                       # CREA la sesión principal de Spark, que usará todo el proyecto
        logger.info("SparkSession creada correctamente")                                            # REGISTRA que la sesión de Spark se creó sin errores

        ejecutar_todos_los_pipelines(spark)                 # EJECUTA el lote completo de pipelines usando la SparkSession creada
        logger.info("La ejecución completa de todos los pipelines finalizó correctamente")          # REGISTRA que el lote terminó con éxito

    except Exception as error:                                                                  # captura cualquier error no controlado que ocurra durante la ejecución global
        logger.error(f"Ocurrió un error durante la ejecución principal: {error}")                   # REGISTRA el mensaje del error para diagnóstico
        raise                                                                                       # vuelve a lanzar la excepción para no ocultar el fallo y permitir que se vea claramente

    finally:                                                                                    # inicia el bloque que siempre se ejecuta, haya habido error o no
        if spark is not None:                                                                       # VERIFICA si la sesión Spark llegó a crearse antes de intentar cerrarla
            spark.stop()                                    # DETIENE la SparkSession y libera los recursos usados por Spark
            logger.info("SparkSession detenida correctamente")                                          # REGISTRA que la sesión de Spark fue cerrada correctamente

        logger.info(f"Finaliza la aplicación principal del pipeline '{NOMBRE_PIPELINE}'")           # REGISTRA el cierre del programa principal


if __name__ == "__main__":                                                                  # VERIFICA si este archivo está siendo ejecutado directamente como un script || El valor de la variable “__name__” (variable dunder) depende de si el archivo se ejecuta DIRECTAMENTE como un “script”, o si el archivo se ejecuto de forma INDIRECTA ---> Esto sucede cuando el acrhivo se ejecuta como un “Modulo”, aquí a la variable “__name__” se le asignara el nombre del modulo.
    main()                                                                                  # LLAMA a la función principal para iniciar la aplicación completa