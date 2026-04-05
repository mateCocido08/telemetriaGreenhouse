"""
Esquemas explícitos de los datasets del proyecto.

Este módulo define la forma esperada de cada dataset: columnas, tipos y nulabilidad.
La validación de rangos, catálogos y duplicados vive en `quality_rules.py`.
"""

from pyspark.sql.types import (
    BooleanType,
    DateType,
    DoubleType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

ESQUEMA_SENSOR_EVENTS = StructType([
    StructField("event_id", StringType(), False),
    StructField("event_time", TimestampType(), False),
    StructField("greenhouse_id", StringType(), False),
    StructField("zone_id", StringType(), False),
    StructField("device_id", StringType(), False),
    StructField("sensor_id", StringType(), False),
    StructField("sensor_type", StringType(), False),
    StructField("topic", StringType(), False),
    StructField("metric_name", StringType(), False),
    StructField("metric_value", DoubleType(), False),
    StructField("unit", StringType(), False),
    StructField("broker_host", StringType(), True),
    StructField("source_system", StringType(), False),
    StructField("ingested_at", TimestampType(), False),
])

ESQUEMA_ACTUATOR_EVENTS = StructType([
    StructField("event_id", StringType(), False),
    StructField("event_time", TimestampType(), False),
    StructField("greenhouse_id", StringType(), False),
    StructField("zone_id", StringType(), False),
    StructField("device_id", StringType(), False),
    StructField("actuator_id", StringType(), False),
    StructField("actuator_type", StringType(), False),
    StructField("topic", StringType(), False),
    StructField("command", StringType(), False),
    StructField("command_value", StringType(), True),
    StructField("command_source", StringType(), False),
    StructField("execution_status", StringType(), False),
    StructField("broker_host", StringType(), True),
    StructField("source_system", StringType(), False),
    StructField("ingested_at", TimestampType(), False),
])

ESQUEMA_DEVICES_MASTER = StructType([
    StructField("device_id", StringType(), False),
    StructField("device_role", StringType(), False),
    StructField("device_type", StringType(), False),
    StructField("sensor_id", StringType(), True),
    StructField("actuator_id", StringType(), True),
    StructField("sensor_type", StringType(), True),
    StructField("actuator_type", StringType(), True),
    StructField("greenhouse_id", StringType(), False),
    StructField("zone_id", StringType(), False),
    StructField("mqtt_topic", StringType(), True),
    StructField("installation_date", DateType(), True),
    StructField("status", StringType(), False),
])

ESQUEMA_ZONES_MASTER = StructType([
    StructField("greenhouse_id", StringType(), False),
    StructField("zone_id", StringType(), False),
    StructField("zone_name", StringType(), False),
    StructField("crop_type", StringType(), True),
    StructField("location_description", StringType(), True),
    StructField("area_m2", DoubleType(), True),
    StructField("is_active", BooleanType(), False),
])

ESQUEMA_WEATHER_API_EVENTS = StructType([
    StructField("weather_event_id", StringType(), False),
    StructField("observed_at", TimestampType(), False),
    StructField("location_id", StringType(), False),
    StructField("location_name", StringType(), False),
    StructField("source_api", StringType(), False),
    StructField("latitude", DoubleType(), False),
    StructField("longitude", DoubleType(), False),
    StructField("outside_temp_c", DoubleType(), True),
    StructField("outside_humidity_pct", DoubleType(), True),
    StructField("precipitation_mm", DoubleType(), True),
    StructField("wind_speed_kmh", DoubleType(), True),
    StructField("cloud_cover_pct", DoubleType(), True),
    StructField("pressure_hpa", DoubleType(), True),
    StructField("ingested_at", TimestampType(), False),
])

ESQUEMAS = {
    "sensor_events": ESQUEMA_SENSOR_EVENTS,
    "actuator_events": ESQUEMA_ACTUATOR_EVENTS,
    "devices_master": ESQUEMA_DEVICES_MASTER,
    "zones_master": ESQUEMA_ZONES_MASTER,
    "weather_api_events": ESQUEMA_WEATHER_API_EVENTS,
}
