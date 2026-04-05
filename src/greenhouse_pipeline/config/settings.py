"""
Configuración central del proyecto.

Este módulo concentra la identidad del pipeline, la configuración base de Spark
y las rutas de entrada/salida usadas por el resto de los módulos.
"""

from pathlib import Path

# Identidad y salida del pipeline
NOMBRE_PIPELINE = "telemetria_greenhouse"
FECHA_EJECUCION = "2026-03-20"
MODO_ESCRITURA = "overwrite"
FORMATO_SALIDA = "parquet"

# Configuración base de Spark
SPARK_APP_NAME = "TelemetriaGreenhousePipeline"
SPARK_MASTER = "local[*]"

# Raíz del proyecto y carpetas principales
RUTA_PROYECTO = Path(__file__).resolve().parents[3]
RUTA_DATA = RUTA_PROYECTO / "data"
RUTA_BRONZE = RUTA_DATA / "bronze"
RUTA_SILVER = RUTA_DATA / "silver"
RUTA_GOLD = RUTA_DATA / "gold"
RUTA_LOGS = RUTA_PROYECTO / "logs"

# Rutas Bronze
RUTA_SENSOR_EVENTS_BRONZE = RUTA_BRONZE / "iot" / "sensor_events.csv"
RUTA_ACTUATOR_EVENTS_BRONZE = RUTA_BRONZE / "iot" / "actuator_events.csv"
RUTA_DEVICES_MASTER_BRONZE = RUTA_BRONZE / "master" / "devices_master.csv"
RUTA_ZONES_MASTER_BRONZE = RUTA_BRONZE / "master" / "zones_master.csv"
RUTA_WEATHER_API_BRONZE = (
    RUTA_BRONZE / "external" / "weather_api" / f"run_date={FECHA_EJECUCION}" / "weather_api_events.json"
)

# Rutas Silver
RUTA_SENSOR_EVENTS_SILVER = RUTA_SILVER / "iot" / "sensor_events"
RUTA_ACTUATOR_EVENTS_SILVER = RUTA_SILVER / "iot" / "actuator_events"
RUTA_DEVICES_MASTER_SILVER = RUTA_SILVER / "master" / "devices_master"
RUTA_ZONES_MASTER_SILVER = RUTA_SILVER / "master" / "zones_master"
RUTA_WEATHER_API_SILVER = RUTA_SILVER / "external" / "weather_api_events"

DATASETS_BRONZE = {
    "sensor_events": RUTA_SENSOR_EVENTS_BRONZE,
    "actuator_events": RUTA_ACTUATOR_EVENTS_BRONZE,
    "devices_master": RUTA_DEVICES_MASTER_BRONZE,
    "zones_master": RUTA_ZONES_MASTER_BRONZE,
    "weather_api_events": RUTA_WEATHER_API_BRONZE,
}

DATASETS_SILVER = {
    "sensor_events": RUTA_SENSOR_EVENTS_SILVER,
    "actuator_events": RUTA_ACTUATOR_EVENTS_SILVER,
    "devices_master": RUTA_DEVICES_MASTER_SILVER,
    "zones_master": RUTA_ZONES_MASTER_SILVER,
    "weather_api_events": RUTA_WEATHER_API_SILVER,
}
