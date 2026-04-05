from pyspark.sql.types import StructType     # importa la estructura principal que representa un esquema completo
from pyspark.sql.types import StructField    # importa la pieza que representa cada columna individual del esquema
from pyspark.sql.types import StringType     # importa el tipo string para textos e identificadores
from pyspark.sql.types import TimestampType  # importa el tipo timestamp para fechas con hora
from pyspark.sql.types import DoubleType     # importa el tipo double para valores numéricos con decimales
from pyspark.sql.types import BooleanType    # importa el tipo boolean para valores verdadero/falso
from pyspark.sql.types import DateType       # importa el tipo date para fechas sin hora

ESQUEMA_SENSOR_EVENTS = StructType([                    # DEFINE EL ESQUEMA COMPLETO DEL DATASET "SENSOR_EVENTS"
    StructField("event_id", StringType(), False),       # define event_id como texto y no permite nulos
    StructField("event_time", TimestampType(), False),  # define event_time como fecha-hora y no permite nulos
    StructField("greenhouse_id", StringType(), False),  # define greenhouse_id como texto y no permite nulos
    StructField("zone_id", StringType(), False),        # define zone_id como texto y no permite nulos
    StructField("device_id", StringType(), False),      # define device_id como texto y no permite nulos
    StructField("sensor_id", StringType(), False),      # define sensor_id como texto y no permite nulos
    StructField("sensor_type", StringType(), False),    # define sensor_type como texto y no permite nulos
    StructField("topic", StringType(), False),          # define topic como texto y no permite nulos
    StructField("metric_name", StringType(), False),    # define metric_name como texto y no permite nulos
    StructField("metric_value", DoubleType(), False),   # define metric_value como número decimal y no permite nulos
    StructField("unit", StringType(), False),           # define unit como texto y no permite nulos
    StructField("broker_host", StringType(), True),     # define broker_host como texto y sí permite nulos
    StructField("source_system", StringType(), False),  # define source_system como texto y no permite nulos
    StructField("ingested_at", TimestampType(), False), # define ingested_at como fecha-hora y no permite nulos
])

ESQUEMA_ACTUATOR_EVENTS = StructType([                    # DEFINE EL ESQUEMA COMPLETO DEL DATASET "ACTUATOR_EVENTS"
    StructField("event_id", StringType(), False),         # define event_id como texto y no permite nulos
    StructField("event_time", TimestampType(), False),    # define event_time como fecha-hora y no permite nulos
    StructField("greenhouse_id", StringType(), False),    # define greenhouse_id como texto y no permite nulos
    StructField("zone_id", StringType(), False),          # define zone_id como texto y no permite nulos
    StructField("device_id", StringType(), False),        # define device_id como texto y no permite nulos
    StructField("actuator_id", StringType(), False),      # define actuator_id como texto y no permite nulos
    StructField("actuator_type", StringType(), False),    # define actuator_type como texto y no permite nulos
    StructField("topic", StringType(), False),            # define topic como texto y no permite nulos
    StructField("command", StringType(), False),          # define command como texto y no permite nulos
    StructField("command_value", StringType(), True),     # define command_value como texto y sí permite nulos
    StructField("command_source", StringType(), False),   # define command_source como texto y no permite nulos
    StructField("execution_status", StringType(), False), # define execution_status como texto y no permite nulos
    StructField("broker_host", StringType(), True),       # define broker_host como texto y sí permite nulos
    StructField("source_system", StringType(), False),    # define source_system como texto y no permite nulos
    StructField("ingested_at", TimestampType(), False),   # define ingested_at como fecha-hora y no permite nulos
])

ESQUEMA_DEVICES_MASTER = StructType([                    # DEFINE EL ESQUEMA COMPLETO DEL DATASET "DEVICES_MASTER"
    StructField("device_id", StringType(), False),       # define device_id como texto y no permite nulos
    StructField("device_role", StringType(), False),     # define device_role como texto y no permite nulos
    StructField("device_type", StringType(), False),     # define device_type como texto y no permite nulos
    StructField("sensor_id", StringType(), True),        # define sensor_id como texto y sí permite nulos
    StructField("actuator_id", StringType(), True),      # define actuator_id como texto y sí permite nulos
    StructField("sensor_type", StringType(), True),      # define sensor_type como texto y sí permite nulos       *
    StructField("actuator_type", StringType(), True),    # define actuator_type como texto y sí permite nulos     *
    StructField("greenhouse_id", StringType(), False),   # define greenhouse_id como texto y no permite nulos
    StructField("zone_id", StringType(), False),         # define zone_id como texto y no permite nulos
    StructField("mqtt_topic", StringType(), True),       # define mqtt_topic como texto y sí permite nulos
    StructField("installation_date", DateType(), True),  # define installation_date como fecha sin hora y sí permite nulos
    StructField("status", StringType(), False),          # define status como texto y no permite nulos
])

ESQUEMA_ZONES_MASTER = StructType([                          # DEFINE EL ESQUEMA COMPLETO DEL DATASET "ZONES_MASTER"
    StructField("greenhouse_id", StringType(), False),       # define greenhouse_id como texto y no permite nulos
    StructField("zone_id", StringType(), False),             # define zone_id como texto y no permite nulos
    StructField("zone_name", StringType(), False),           # define zone_name como texto y no permite nulos
    StructField("crop_type", StringType(), True),            # define crop_type como texto y sí permite nulos
    StructField("location_description", StringType(), True), # define location_description como texto y sí permite nulos
    StructField("area_m2", DoubleType(), True),              # define area_m2 como número decimal y sí permite nulos
    StructField("is_active", BooleanType(), False),          # define is_active como booleano y no permite nulos
])

ESQUEMA_WEATHER_API_EVENTS = StructType([                    # DEFINE EL ESQUEMA COMPLETO DEL DATASET "WEATHER_API_EVENTS" 
    StructField("weather_event_id", StringType(), False),    # define weather_event_id como texto y no permite nulos
    StructField("observed_at", TimestampType(), False),      # define observed_at como fecha-hora y no permite nulos
    StructField("location_id", StringType(), False),         # define location_id como texto y no permite nulos
    StructField("location_name", StringType(), False),       # define location_name como texto y no permite nulos
    StructField("source_api", StringType(), False),          # define source_api como texto y no permite nulos
    StructField("latitude", DoubleType(), False),            # define latitude como número decimal y no permite nulos
    StructField("longitude", DoubleType(), False),           # define longitude como número decimal y no permite nulos
    StructField("outside_temp_c", DoubleType(), True),       # define outside_temp_c como número decimal y sí permite nulos
    StructField("outside_humidity_pct", DoubleType(), True), # define outside_humidity_pct como número decimal y sí permite nulos
    StructField("precipitation_mm", DoubleType(), True),     # define precipitation_mm como número decimal y sí permite nulos
    StructField("wind_speed_kmh", DoubleType(), True),       # define wind_speed_kmh como número decimal y sí permite nulos
    StructField("cloud_cover_pct", DoubleType(), True),      # define cloud_cover_pct como número decimal y sí permite nulos
    StructField("pressure_hpa", DoubleType(), True),         # define pressure_hpa como número decimal y sí permite nulos
    StructField("ingested_at", TimestampType(), False),      # define ingested_at como fecha-hora y no permite nulos
])

ESQUEMAS = {                                          # AGRUPA TODOS LOS ESQUEMAS EN UN SOLO DICCIONARIO para acceder a ellos por su nombre
    "sensor_events": ESQUEMA_SENSOR_EVENTS,           # guarda el esquema de sensor_events bajo una clave clara
    "actuator_events": ESQUEMA_ACTUATOR_EVENTS,       # guarda el esquema de actuator_events bajo una clave clara
    "devices_master": ESQUEMA_DEVICES_MASTER,         # guarda el esquema de devices_master bajo una clave clara
    "zones_master": ESQUEMA_ZONES_MASTER,             # guarda el esquema de zones_master bajo una clave clara
    "weather_api_events": ESQUEMA_WEATHER_API_EVENTS, # guarda el esquema de weather_api_events bajo una clave clara
}



''' 
scehmas.py
Responde:
    - qué columnas tiene cada dataset
    - qué tipo de dato tiene cada columna
    - cuáles admiten nulos y cuáles no
    
    En una frase
        - settings.py organiza el territorio
        - schemas.py organiza la forma de los datos
        

schemas.py no:
    - valida rangos
    - valida valores permitidos
    - detecta duplicados
    - limpia datos
    - transforma datos
    - escribe archivos

Eso lo harán otros módulos.

schemas.py: Solo define la estructura esperada.

====================================================================

Relación con los otros archivos

readers.py
    - Usará schemas.py para leer con el tipo correcto.

validators.py
    - Usará schemas.py para comprobar estructura esperada.

transformers.py
    - Partirá de datasets que ya respetan estos tipos.

writers.py
    - Escribirá datasets que ya fueron modelados según estos esquemas.



====================================================================
Explicación línea por línea

1) Esquema de sensor_events

ESQUEMA_SENSOR_EVENTS = StructType([... ])

    - Crea una variable llamada ESQUEMA_SENSOR_EVENTS.
    - Su valor define el esquema completo del dataset sensor_events
    - StructType([ ... ]) significa:  “voy a construir una tabla formada por varias columnas”


StructField("event_id", StringType(), False),

    Este StructField tiene tres partes:
        - "event_id" → nombre de la columna
        - StringType() → tipo de dato (texto)
        - False → no permite nulos (obligatorio)
        
        
StructField("event_time", TimestampType(), False),

        - "event_time" → nombre de la columna
        - TimestampType() → tipo de dato (fecha con hora)
        - False → no permite nulos (obligatorio)
        - sirve para saber cuándo ocurrió el evento        


StructField("greenhouse_id", StringType(), False),
        - guarda el identificador del invernadero
        - como texto
        - obligatorio

StructField("zone_id", StringType(), False),
        - guarda la zona interna
        - también como texto obligatorio

StructField("device_id", StringType(), False),
        - guarda qué dispositivo emitió el evento

StructField("sensor_id", StringType(), False),
        - guarda qué sensor lógico generó la medición

StructField("sensor_type", StringType(), False),
        - guarda el tipo de sensor
          por ejemplo:
            - dht22
            - tsl2561

StructField("topic", StringType(), False),
        - guarda el tópico MQTT original

StructField("metric_name", StringType(), False),
        - guarda el nombre de la métrica
          por ejemplo:
            - air_temperature
            - air_humidity

StructField("metric_value", DoubleType(), False),
        - guarda el valor medido
        - como número decimal
        - obligatorio

StructField("unit", StringType(), False),
        - guarda la unidad de medida
          por ejemplo:
            - celsius
            - percent
            - lux

StructField("broker_host", StringType(), True),
        - guarda el broker MQTT
        - puede quedar nulo (True)

StructField("source_system", StringType(), False),
        - indica desde qué sistema llegó el dato
          por ejemplo:
            - mqtt_esp32
            - node_red_export

StructField("ingested_at", TimestampType(), False),
        - registra cuándo fue ingerido el dato
        - obligatorio
])



====================================================================
2) esquema de actuator_events 

Qué tarea cumple:
Define cómo debe verse el dataset de eventos de actuadores.

Explicación conceptual:
Se parece mucho a sensor_events, pero cambia el foco:
"ya no habla de métricas medidas, ahora habla de comandos o acciones ejecutadas"

Campos importantes nuevos:
actuator_id
    - identifica el actuador lógico
      por ejemplo:
        - una válvula de riego
        
actuator_type
    - identifica el tipo
      por ejemplo:
    - irrigation_valve
    - air_extractor
    
command
    - indica la acción
      por ejemplo:
        - turn_on
        - turn_off

command_value
    - guarda un valor asociado al comando
    - puede ser nulo
    - por eso se usa True
    
command_source
    - indica quién emitió la orden
      por ejemplo:
        - blynk
        - automatic_rule
        
execution_status
    dice si la orden fue:
        - recibida
        - ejecutada
        - fallida



====================================================================
3) Esquema de devices_master

Qué tarea cumple:
    Define la estructura de la tabla maestra de dispositivos.

Idea clave:
    Este dataset no guarda eventos.
    Guarda catálogo.

Es decir:
    -qué dispositivos existen
    -qué rol cumplen
    -dónde están
    -en qué estado están
    
    
Explicación de campos importantes:

device_id
    -clave principal del dispositivo
    
device_role
    -indica su papel en la arquitectura
    por ejemplo:
        -sensor_node
        -actuator_node
        -gateway
        
device_type
    -indica el tipo físico o técnico
    por ejemplo:
        - esp32
        - raspberry_pi
        
sensor_id
    -puede existir o no
    -porque no todos los dispositivos son sensores

actuator_id
    -puede existir o no
    -porque no todos los dispositivos son actuadores

installation_date
    -usa DateType()
    -porque alcanza con la fecha
    -no hace falta la hora exacta

status
    -indica si el dispositivo está:
    -activo
    -en mantenimiento
    -inactivo



====================================================================
4) esquema de zones_master

Qué tarea cumple:
Define la estructura de la tabla maestra de zonas del invernadero.

Idea clave:
También es una tabla de catálogo, no de eventos.

Campos importantes:
zone_name
    -nombre humano de la zona
    por ejemplo:
        propagation
        seedlings
        crop_type
        
tipo de cultivo
    -puede ser nulo en esta etapa
    
location_description
    -texto descriptivo de la ubicación
    
area_m2
    -superficie de la zona
    -por eso se usa DoubleType()
    
is_active
    -indica si la zona está activa   
    usa BooleanType()
    solo admite:
        -True
        -False



====================================================================
5) esquema de weather_api_events
Qué tarea cumple:
    -Define la estructura del dataset que viene de la API meteorológica.

Idea clave:
    -Este dataset es una fuente externa de contexto.
    -No mide dentro del invernadero.
    -Mide las condiciones de afuera.

Explicación de campos importantes:
    -weather_event_id
    -identifica cada observación meteorológica

observed_at
    -indica cuándo fue registrada por la API

source_api
    -identifica qué API la produjo

latitude y longitude
    -representan ubicación geográfica
    -por eso son DoubleType()

outside_temp_c
    -temperatura exterior

outside_humidity_pct
    -humedad exterior

precipitation_mm
    -lluvia acumulada

wind_speed_kmh
    -velocidad del viento

cloud_cover_pct
    -porcentaje de nubosidad

pressure_hpa
    -presión atmosférica

'''