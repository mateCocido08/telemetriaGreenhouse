"""
Reglas de calidad declarativas por dataset.

Se separan de `schemas.py` para distinguir entre forma estructural del dato
y criterios de aceptabilidad usados durante la validación.
"""

COLUMNAS_REQUERIDAS = {
    "sensor_events": [
        "event_id",
        "event_time",
        "greenhouse_id",
        "zone_id",
        "device_id",
        "sensor_id",
        "sensor_type",
        "topic",
        "metric_name",
        "metric_value",
        "unit",
        "source_system",
        "ingested_at",
    ],
    "actuator_events": [
        "event_id",
        "event_time",
        "greenhouse_id",
        "zone_id",
        "device_id",
        "actuator_id",
        "actuator_type",
        "topic",
        "command",
        "command_source",
        "execution_status",
        "source_system",
        "ingested_at",
    ],
    "devices_master": [
        "device_id",
        "device_role",
        "device_type",
        "greenhouse_id",
        "zone_id",
        "status",
    ],
    "zones_master": [
        "greenhouse_id",
        "zone_id",
        "zone_name",
        "is_active",
    ],
    "weather_api_events": [
        "weather_event_id",
        "observed_at",
        "location_id",
        "location_name",
        "source_api",
        "latitude",
        "longitude",
        "ingested_at",
    ],
}

COLUMNAS_NO_NULAS = {
    "sensor_events": [
        "event_id",
        "event_time",
        "greenhouse_id",
        "zone_id",
        "device_id",
        "sensor_id",
        "sensor_type",
        "topic",
        "metric_name",
        "metric_value",
        "unit",
        "source_system",
        "ingested_at",
    ],
    "actuator_events": [
        "event_id",
        "event_time",
        "greenhouse_id",
        "zone_id",
        "device_id",
        "actuator_id",
        "actuator_type",
        "topic",
        "command",
        "command_source",
        "execution_status",
        "source_system",
        "ingested_at",
    ],
    "devices_master": [
        "device_id",
        "device_role",
        "device_type",
        "greenhouse_id",
        "zone_id",
        "status",
    ],
    "zones_master": [
        "greenhouse_id",
        "zone_id",
        "zone_name",
        "is_active",
    ],
    "weather_api_events": [
        "weather_event_id",
        "observed_at",
        "location_id",
        "location_name",
        "source_api",
        "latitude",
        "longitude",
        "ingested_at",
    ],
}

VALORES_PERMITIDOS = {
    "sensor_events": {
        "sensor_type": [
            "dht22",
            "tsl2561",
            "soil_moisture_capacitive",
        ],
        "metric_name": [
            "air_temperature",
            "air_humidity",
            "soil_moisture",
            "light_intensity",
        ],
        "unit": [
            "celsius",
            "percent",
            "lux",
        ],
        "source_system": [
            "mqtt_esp32",
            "node_red_export",
            "python_subscriber",
        ],
    },
    "actuator_events": {
        "actuator_type": [
            "irrigation_valve",
            "air_injector",
            "air_extractor",
        ],
        "command": [
            "turn_on",
            "turn_off",
        ],
        "command_source": [
            "blynk",
            "node_red",
            "automatic_rule",
            "manual_override",
        ],
        "execution_status": [
            "received",
            "executed",
            "failed",
        ],
        "source_system": [
            "mqtt_esp32",
            "node_red_export",
            "python_subscriber",
        ],
    },
    "devices_master": {
        "device_role": [
            "sensor_node",
            "actuator_node",
            "gateway",
            "broker",
        ],
        "device_type": [
            "esp32",
            "raspberry_pi",
            "relay_module",
            "sensor_module",
        ],
        "sensor_type": [
            "dht22",
            "tsl2561",
            "soil_moisture_capacitive",
        ],
        "actuator_type": [
            "irrigation_valve",
            "air_injector",
            "air_extractor",
        ],
        "status": [
            "active",
            "maintenance",
            "inactive",
        ],
    },
    "zones_master": {},
    "weather_api_events": {},
}

RANGOS_NUMERICOS = {
    "sensor_events": {
        # En sensor_events, el rango aceptable de metric_value depende de metric_name.
        "metric_value": {
            "air_temperature": {"min": -10.0, "max": 60.0},
            "air_humidity": {"min": 0.0, "max": 100.0},
            "soil_moisture": {"min": 0.0, "max": 100.0},
            "light_intensity": {"min": 0.0, "max": 120000.0},
        },
    },
    "actuator_events": {},
    "devices_master": {
        "installation_date": {},
    },
    "zones_master": {
        "area_m2": {"min": 0.0, "max": 100000.0},
    },
    "weather_api_events": {
        "latitude": {"min": -90.0, "max": 90.0},
        "longitude": {"min": -180.0, "max": 180.0},
        "outside_temp_c": {"min": -40.0, "max": 60.0},
        "outside_humidity_pct": {"min": 0.0, "max": 100.0},
        "precipitation_mm": {"min": 0.0, "max": 500.0},
        "wind_speed_kmh": {"min": 0.0, "max": 250.0},
        "cloud_cover_pct": {"min": 0.0, "max": 100.0},
        "pressure_hpa": {"min": 800.0, "max": 1100.0},
    },
}

COLUMNAS_CLAVE_DUPLICADOS = {
    "sensor_events": ["event_time", "sensor_id", "metric_name"],
    "actuator_events": ["event_time", "actuator_id", "command"],
    "devices_master": ["device_id"],
    "zones_master": ["zone_id"],
    "weather_api_events": ["observed_at", "location_id"],
}

REGLAS_CALIDAD = {
    "sensor_events": {
        "columnas_requeridas": COLUMNAS_REQUERIDAS["sensor_events"],
        "columnas_no_nulas": COLUMNAS_NO_NULAS["sensor_events"],
        "valores_permitidos": VALORES_PERMITIDOS["sensor_events"],
        "rangos_numericos": RANGOS_NUMERICOS["sensor_events"],
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["sensor_events"],
    },
    "actuator_events": {
        "columnas_requeridas": COLUMNAS_REQUERIDAS["actuator_events"],
        "columnas_no_nulas": COLUMNAS_NO_NULAS["actuator_events"],
        "valores_permitidos": VALORES_PERMITIDOS["actuator_events"],
        "rangos_numericos": RANGOS_NUMERICOS["actuator_events"],
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["actuator_events"],
    },
    "devices_master": {
        "columnas_requeridas": COLUMNAS_REQUERIDAS["devices_master"],
        "columnas_no_nulas": COLUMNAS_NO_NULAS["devices_master"],
        "valores_permitidos": VALORES_PERMITIDOS["devices_master"],
        "rangos_numericos": RANGOS_NUMERICOS["devices_master"],
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["devices_master"],
    },
    "zones_master": {
        "columnas_requeridas": COLUMNAS_REQUERIDAS["zones_master"],
        "columnas_no_nulas": COLUMNAS_NO_NULAS["zones_master"],
        "valores_permitidos": VALORES_PERMITIDOS["zones_master"],
        "rangos_numericos": RANGOS_NUMERICOS["zones_master"],
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["zones_master"],
    },
    "weather_api_events": {
        "columnas_requeridas": COLUMNAS_REQUERIDAS["weather_api_events"],
        "columnas_no_nulas": COLUMNAS_NO_NULAS["weather_api_events"],
        "valores_permitidos": VALORES_PERMITIDOS["weather_api_events"],
        "rangos_numericos": RANGOS_NUMERICOS["weather_api_events"],
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["weather_api_events"],
    },
}
