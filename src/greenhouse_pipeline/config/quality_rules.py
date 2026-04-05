COLUMNAS_REQUERIDAS = {     # agrupa las COLUMNAS QUE DEBEN EXISTIR en cada dataset
    "sensor_events": [      # define la lista de COLUMNAS OBLIGATORIAS del dataset sensor_events
        "event_id",         # exige que exista la columna event_id
        "event_time",       # exige que exista la columna event_time
        "greenhouse_id",    # exige que exista la columna greenhouse_id
        "zone_id",          # exige que exista la columna zone_id
        "device_id",        # exige que exista la columna device_id
        "sensor_id",        # exige que exista la columna sensor_id
        "sensor_type",      # exige que exista la columna sensor_type      *
        "topic",            # exige que exista la columna topic
        "metric_name",      # exige que exista la columna metric_name      *
        "metric_value",     # exige que exista la columna metric_value
        "unit",             # exige que exista la columna unit             *
        "source_system",    # exige que exista la columna source_system    *
        "ingested_at",      # exige que exista la columna ingested_at
    ],                     
    "actuator_events": [    # define la lista de COLUMNAS OBLIGATORIAS del dataset actuator_events
        "event_id",         # exige que exista la columna event_id
        "event_time",       # exige que exista la columna event_time
        "greenhouse_id",    # exige que exista la columna greenhouse_id
        "zone_id",          # exige que exista la columna zone_id
        "device_id",        # exige que exista la columna device_id
        "actuator_id",      # exige que exista la columna actuator_id
        "actuator_type",    # exige que exista la columna actuator_type     *
        "topic",            # exige que exista la columna topic
        "command",          # exige que exista la columna command           *
        "command_source",   # exige que exista la columna command_source    *
        "execution_status", # exige que exista la columna execution_status  *
        "source_system",    # exige que exista la columna source_system     *
        "ingested_at",      # exige que exista la columna ingested_at
    ], 
    "devices_master": [     # define la lista de COLUMNAS OBLIGATORIAS del dataset devices_master
        "device_id",        # exige que exista la columna device_id
        "device_role",      # exige que exista la columna device_role     *
        "device_type",      # exige que exista la columna device_type     *
        "greenhouse_id",    # exige que exista la columna greenhouse_id
        "zone_id",          # exige que exista la columna zone_id
        "status",           # exige que exista la columna status          *
    ],  
    "zones_master": [       # define la lista de COLUMNAS OBLIGATORIAS del dataset zones_master
        "greenhouse_id",    # exige que exista la columna greenhouse_id
        "zone_id",          # exige que exista la columna zone_id
        "zone_name",        # exige que exista la columna zone_name
        "is_active",        # exige que exista la columna is_active
    ],  
    "weather_api_events": [ # define la lista de COLUMNAS OBLIGATORIAS del dataset weather_api_events
        "weather_event_id", # exige que exista la columna weather_event_id
        "observed_at",      # exige que exista la columna observed_at
        "location_id",      # exige que exista la columna location_id
        "location_name",    # exige que exista la columna location_name
        "source_api",       # exige que exista la columna source_api
        "latitude",         # exige que exista la columna latitude
        "longitude",        # exige que exista la columna longitude
        "ingested_at",      # exige que exista la columna ingested_at
    ],  
} 

COLUMNAS_NO_NULAS = {       # agrupa las columnas que además de existir no pueden venir con valores nulos
    "sensor_events": [      # define las COLUMNAS NO NULAS del dataset sensor_events
        "event_id",         # obliga a que event_id tenga valor
        "event_time",       # obliga a que event_time tenga valor
        "greenhouse_id",    # obliga a que greenhouse_id tenga valor
        "zone_id",          # obliga a que zone_id tenga valor
        "device_id",        # obliga a que device_id tenga valor
        "sensor_id",        # obliga a que sensor_id tenga valor
        "sensor_type",      # obliga a que sensor_type tenga valor
        "topic",            # obliga a que topic tenga valor
        "metric_name",      # obliga a que metric_name tenga valor
        "metric_value",     # obliga a que metric_value tenga valor
        "unit",             # obliga a que unit tenga valor
        "source_system",    # obliga a que source_system tenga valor
        "ingested_at",      # obliga a que ingested_at tenga valor
    ],  
    "actuator_events": [    # define las COLUMNAS NO NULAS del dataset actuator_events
        "event_id",         # obliga a que event_id tenga valor
        "event_time",       # obliga a que event_time tenga valor
        "greenhouse_id",    # obliga a que greenhouse_id tenga valor
        "zone_id",          # obliga a que zone_id tenga valor
        "device_id",        # obliga a que device_id tenga valor
        "actuator_id",      # obliga a que actuator_id tenga valor
        "actuator_type",    # obliga a que actuator_type tenga valor
        "topic",            # obliga a que topic tenga valor
        "command",          # obliga a que command tenga valor
        "command_source",   # obliga a que command_source tenga valor
        "execution_status", # obliga a que execution_status tenga valor
        "source_system",    # obliga a que source_system tenga valor
        "ingested_at",      # obliga a que ingested_at tenga valor
    ],  
    "devices_master": [     # define las COLUMNAS NO NULAS del dataset devices_master
        "device_id",        # obliga a que device_id tenga valor
        "device_role",      # obliga a que device_role tenga valor
        "device_type",      # obliga a que device_type tenga valor
        "greenhouse_id",    # obliga a que greenhouse_id tenga valor
        "zone_id",          # obliga a que zone_id tenga valor
        "status",           # obliga a que status tenga valor
    ], 
    "zones_master": [       # define las COLUMNAS NO NULAS del dataset zones_master
        "greenhouse_id",    # obliga a que greenhouse_id tenga valor
        "zone_id",          # obliga a que zone_id tenga valor
        "zone_name",        # obliga a que zone_name tenga valor
        "is_active",        # obliga a que is_active tenga valor
    ],  
    "weather_api_events": [ # define las COLUMNAS NO NULASs del dataset weather_api_events
        "weather_event_id", # obliga a que weather_event_id tenga valor
        "observed_at",      # obliga a que observed_at tenga valor
        "location_id",      # obliga a que location_id tenga valor
        "location_name",    # obliga a que location_name tenga valor
        "source_api",       # obliga a que source_api tenga valor
        "latitude",         # obliga a que latitude tenga valor
        "longitude",        # obliga a que longitude tenga valor
        "ingested_at",      # obliga a que ingested_at tenga valor
    ],  
}  

VALORES_PERMITIDOS = {                  # agrupa catálogos de VALORES VÁLIDOS POR DATASET y por columna
    "sensor_events": {                  # define las reglas de catálogo del dataset sensor_events
        "sensor_type": [                # define los VALORES ACEPTADOS para sensor_type
            "dht22",                    # permite el tipo de sensor dht22
            "tsl2561",                  # permite el tipo de sensor tsl2561
            "soil_moisture_capacitive", # permite el tipo de sensor de humedad de suelo capacitivo
        ],  
        "metric_name": [                # define los VALORES ACEPTADOS para metric_name
            "air_temperature",          # permite la métrica de temperatura ambiente        * se le definio un rango
            "air_humidity",             # permite la métrica de humedad ambiente            * se le definio un rango
            "soil_moisture",            # permite la métrica de humedad de suelo            * se le definio un rango
            "light_intensity",          # permite la métrica de intensidad lumínica         * se le definio un rango
        ],  
        "unit": [                       # define los VALORES ACEPTADOS para unit
            "celsius",                  # permite la unidad celsius
            "percent",                  # permite la unidad percent
            "lux",                      # permite la unidad lux
        ], 
        "source_system": [              # define los VALORES ACEPTADOS para source_system
            "mqtt_esp32",               # permite como origen el publicador mqtt_esp32
            "node_red_export",          # permite como origen una exportación de node-red
            "python_subscriber",        # permite como origen un suscriptor python
        ],  
    },  
    "actuator_events": {                # define las reglas de catálogo del dataset actuator_events
        "actuator_type": [              # define los VALORES ACEPTADOS para actuator_type
            "irrigation_valve",         # permite actuadores de válvula de riego
            "air_injector",             # permite actuadores de inyección de aire
            "air_extractor",            # permite actuadores de extracción de aire
        ], 
        "command": [                    # define los VALORES ACEPTADOS para command
            "turn_on",                  # permite el comando de encendido
            "turn_off",                 # permite el comando de apagado
        ],  
        "command_source": [             # define los VALORES ACEPTADOS para command_source
            "blynk",                    # permite como emisor del comando a blynk
            "node_red",                 # permite como emisor del comando a node-red
            "automatic_rule",           # permite como emisor una regla automática
            "manual_override",          # permite como emisor una intervención manual
        ],  
        "execution_status": [           # define los VALORES ACEPTADOS para execution_status
            "received",                 # permite el estado received
            "executed",                 # permite el estado executed
            "failed",                   # permite el estado failed
        ],  
        "source_system": [              # define los VALORES ACEPTADOS para source_system
            "mqtt_esp32",               # permite como origen el publicador mqtt_esp32
            "node_red_export",          # permite como origen una exportación de node-red
            "python_subscriber",        # permite como origen un suscriptor python
        ], 
    }, 
    "devices_master": {                 # define las reglas de catálogo del dataset devices_master
        "device_role": [                # define los VALORES ACEPTADOS para device_role
            "sensor_node",              # permite el rol de nodo sensor
            "actuator_node",            # permite el rol de nodo actuador
            "gateway",                  # permite el rol de gateway
            "broker",                   # permite el rol de broker
        ], 
        "device_type": [                # define los VALORES ACEPTADOS para device_type
            "esp32",                    # permite el tipo de dispositivo esp32
            "raspberry_pi",             # permite el tipo de dispositivo raspberry_pi
            "relay_module",             # permite el tipo de dispositivo relay_module
            "sensor_module",            # permite el tipo de dispositivo sensor_module
        ], 
        "sensor_type": [                # define los VALORES ACEPTADOS para sensor_type
            "dht22",                    # permite el tipo de sensor dht22
            "tsl2561",                  # permite el tipo de sensor tsl2561
            "soil_moisture_capacitive", # permite el tipo de sensor de humedad de suelo capacitivo
        ], 
        "actuator_type": [              # define los VALORES ACEPTADOS para actuator_type
            "irrigation_valve",         # permite actuadores de válvula de riego
            "air_injector",             # permite actuadores de inyección de aire
            "air_extractor",            # permite actuadores de extracción de aire
        ],
        "status": [                     # define los VALORES ACEPTADOS para status
            "active",                   # permite el estado active
            "maintenance",              # permite el estado maintenance
            "inactive",                 # permite el estado inactive
        ],  
    },  
    "zones_master": {},                 # deja SIN CATALOGOS FIJOS al dataset zones_master en esta primera versión
    "weather_api_events": {},           # deja SIN CATALOGOS FIJOS al dataset weather_api_events en esta primera versión
} 

RANGOS_NUMERICOS = {                                            # agrupa los RANGOS VALIDOS para columnas numéricas por dataset
    "sensor_events": {                                          # define los RANGOS NUMÉRICOS ACEPTADOS del dataset sensor_events
        "metric_value": {                                       # agrupa subrangos según el tipo de métrica
            "air_temperature": {"min": -10.0, "max": 60.0},     # define el RANGO ACEPTADO de temperatura ambiente
            "air_humidity": {"min": 0.0, "max": 100.0},         # define el RANGO ACEPTADO de humedad ambiente
            "soil_moisture": {"min": 0.0, "max": 100.0},        # define el RANGO ACEPTADO de humedad de suelo
            "light_intensity": {"min": 0.0, "max": 120000.0},   # define el RANGO ACEPTADO de intensidad lumínica
        }, 
    }, 
    "actuator_events": {},          # no define rangos numéricos para actuator_events en esta primera versión
    "devices_master": {             # define los rangos numéricos del dataset devices_master
        "installation_date": {},    # deja este campo sin rango numérico porque es una fecha y no se valida aquí
    },  
    "zones_master": {                               # define los rangos numéricos del dataset zones_master
        "area_m2": {"min": 0.0, "max": 100000.0},   # define un rango razonable de superficie en metros cuadrados
    }, 
    "weather_api_events": {                                 # define los rangos numéricos del dataset weather_api_events
        "latitude": {"min": -90.0, "max": 90.0},            # define el RANGO VÁLIDO de latitud
        "longitude": {"min": -180.0, "max": 180.0},         # define el RANGO VÁLIDO de longitud
        "outside_temp_c": {"min": -40.0, "max": 60.0},      # define el RANGO VÁLIDO de temperatura exterior
        "outside_humidity_pct": {"min": 0.0, "max": 100.0}, # define el RANGO VÁLIDO de humedad exterior
        "precipitation_mm": {"min": 0.0, "max": 500.0},     # define el RANGO VÁLIDO de precipitación
        "wind_speed_kmh": {"min": 0.0, "max": 250.0},       # define el RANGO VÁLIDO de velocidad del viento
        "cloud_cover_pct": {"min": 0.0, "max": 100.0},      # define el RANGO VÁLIDO de nubosidad
        "pressure_hpa": {"min": 800.0, "max": 1100.0},      # define el RANGO VÁLIDO de presión atmosférica
    }, 
} 

COLUMNAS_CLAVE_DUPLICADOS = {                                       # agrupa las columnas que se usarán para detectar filas duplicadas por dataset
    "sensor_events": ["event_time", "sensor_id", "metric_name"],    # define la CLAVE NATURAL para buscar duplicados en sensor_events
    "actuator_events": ["event_time", "actuator_id", "command"],    # define la CLAVE NATURAL para buscar duplicados en actuator_events
    "devices_master": ["device_id"],                                # define la CLAVE NATURAL para buscar duplicados en devices_master
    "zones_master": ["zone_id"],                                    # define la CLAVE NATURAL para buscar duplicados en zones_master
    "weather_api_events": ["observed_at", "location_id"],           # define la CLAVE NATURAL para buscar duplicados en weather_api_events
}  

REGLAS_CALIDAD = {                                                      # agrupa en una sola estructura todas las reglas de calidad por dataset
    "sensor_events": {                                                  # reúne las REGLAS DE CALIDAD del dataset sensor_events
        "columnas_requeridas": COLUMNAS_REQUERIDAS["sensor_events"],    # enlaza las "columnas requeridas" de sensor_events
        "columnas_no_nulas": COLUMNAS_NO_NULAS["sensor_events"],        # enlaza las "columnas no nulas" de sensor_events
        "valores_permitidos": VALORES_PERMITIDOS["sensor_events"],      # enlaza los "catálogos válidos" de sensor_events
        "rangos_numericos": RANGOS_NUMERICOS["sensor_events"],          # enlaza los "rangos numéricos" de sensor_events
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["sensor_events"], # enlaza la clave de duplicados de sensor_events
    },  
    "actuator_events": {                                                # reúne las REGLAS DE CALIDAD del dataset actuator_events
        "columnas_requeridas": COLUMNAS_REQUERIDAS["actuator_events"],  # enlaza las "columnas requeridas" de actuator_events
        "columnas_no_nulas": COLUMNAS_NO_NULAS["actuator_events"],      # enlaza las "columnas no nulas" de actuator_events
        "valores_permitidos": VALORES_PERMITIDOS["actuator_events"],    # enlaza los "catálogos válidos" de actuator_events
        "rangos_numericos": RANGOS_NUMERICOS["actuator_events"],        # enlaza los "rangos numéricos" de actuator_events
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["actuator_events"], # enlaza la clave de duplicados de actuator_events
    },  
    "devices_master": {                                                 # reúne las REGLAS DE CALIDAD del dataset devices_master
        "columnas_requeridas": COLUMNAS_REQUERIDAS["devices_master"],   # enlaza las "columnas requeridas" de devices_master
        "columnas_no_nulas": COLUMNAS_NO_NULAS["devices_master"],       # enlaza las "columnas no nulas" de devices_master
        "valores_permitidos": VALORES_PERMITIDOS["devices_master"],     # enlaza los "catálogos válidos" de devices_master
        "rangos_numericos": RANGOS_NUMERICOS["devices_master"],         # enlaza los "rangos numéricos" de devices_master
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["devices_master"],  # enlaza la clave de duplicados de devices_master
    }, 
    "zones_master": {                                                   # reúne las REGLAS DE CALIDAD del dataset zones_master
        "columnas_requeridas": COLUMNAS_REQUERIDAS["zones_master"],     # enlaza las "columnas requeridas" de zones_master
        "columnas_no_nulas": COLUMNAS_NO_NULAS["zones_master"],         # enlaza las "columnas no nulas" de zones_master
        "valores_permitidos": VALORES_PERMITIDOS["zones_master"],       # enlaza los "catálogos válidos" de zones_master
        "rangos_numericos": RANGOS_NUMERICOS["zones_master"],           # enlaza los "rangos numéricos" de zones_master
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["zones_master"],  # enlaza la clave de duplicados de zones_master
    }, 
    "weather_api_events": {                                                 # reúne las REGLAS DE CALIDAD del dataset weather_api_events
        "columnas_requeridas": COLUMNAS_REQUERIDAS["weather_api_events"],   # enlaza las "columnas requeridas" de weather_api_events
        "columnas_no_nulas": COLUMNAS_NO_NULAS["weather_api_events"],       # enlaza las "columnas no nulas" de weather_api_events
        "valores_permitidos": VALORES_PERMITIDOS["weather_api_events"],     # enlaza los "catálogos válidos" de weather_api_events
        "rangos_numericos": RANGOS_NUMERICOS["weather_api_events"],         # enlaza los "rangos numéricos" de weather_api_events
        "columnas_clave_duplicados": COLUMNAS_CLAVE_DUPLICADOS["weather_api_events"],  # enlaza la clave de duplicados de weather_api_events
    }, 
} 