from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType

from greenhouse_pipeline.config.schemas import ESQUEMAS
from greenhouse_pipeline.config.settings import DATASETS_BRONZE


def obtener_ruta_dataset_bronze(nombre_dataset: str) -> str:
    if nombre_dataset not in DATASETS_BRONZE:
        raise KeyError(f"No existe ruta bronze configurada para el dataset: {nombre_dataset}")
    return str(DATASETS_BRONZE[nombre_dataset])


def obtener_esquema_dataset(nombre_dataset: str) -> StructType:
    if nombre_dataset not in ESQUEMAS:
        raise KeyError(f"No existe esquema configurado para el dataset: {nombre_dataset}")
    return ESQUEMAS[nombre_dataset]


def leer_csv_con_esquema(
    spark: SparkSession,
    ruta_archivo: str,
    esquema: StructType,
) -> DataFrame:
    return (
        spark.read
        .option("header", "true")
        .option("sep", ",")
        .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
        .option("dateFormat", "yyyy-MM-dd")
        .schema(esquema)
        .csv(ruta_archivo)
    )


def leer_json_con_esquema(
    spark: SparkSession,
    ruta_archivo: str,
    esquema: StructType,
) -> DataFrame:
    return (
        spark.read
        .option("multiline", "true")
        .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
        .option("dateFormat", "yyyy-MM-dd")
        .schema(esquema)
        .json(ruta_archivo)
    )


def leer_dataset_bronze(
    spark: SparkSession,
    nombre_dataset: str,
) -> DataFrame:
    ruta_dataset = obtener_ruta_dataset_bronze(nombre_dataset)
    esquema_dataset = obtener_esquema_dataset(nombre_dataset)

    if nombre_dataset == "weather_api_events":
        return leer_json_con_esquema(spark, ruta_dataset, esquema_dataset)

    return leer_csv_con_esquema(spark, ruta_dataset, esquema_dataset)
