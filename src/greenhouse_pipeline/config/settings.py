# 1) Importacion de herramienta para manejar rutas
from pathlib import Path        # importa Path para trabajar con rutas de forma segura y legible.

# 2) Definicion de la identidad básica del PIPELINE (Centraliza los parámetros más generales del proyecto.)
NOMBRE_PIPELINE = "telemetria_greenhouse"   # define el nombre general del pipeline.
FECHA_EJECUCION = "2026-03-20"              # define una fecha de ejecución fija para esta primera versión, esa fecha se usa para construir rutas con "run_date=...".Es fija pero mas adelante podría volverse dinámica. (esta fecha no es automática todavía. Es una simplificación intencional.)
MODO_ESCRITURA = "overwrite"                # indica que la escritura en la ruta de salida (Silver), reemplazará datos si ya existen.
FORMATO_SALIDA = "parquet"                  # define el formato final de almacenamiento en la capa silver (o ruta de salida).

# 3) Definicion de la configuración base de SPARK. Le dice a Spark cómo identificarse y cómo ejecutarse.
SPARK_APP_NAME = "TelemetriaGreenhousePipeline" # define el nombre de la aplicación Spark
SPARK_MASTER = "local[*]"                       # indica que Spark correrá en modo local usando todos los núcleos disponibles || local significa: no clúster, no nube, no servidor remoto. 

# 4) Calculo de la RAIZ del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parents[3]  # calcula automáticamente la ruta a la carpeta raíz del proyecto. Descubre dónde está la carpeta principal del repo, sin que tengas que escribirla a mano. 

##################
##### RUTAS ######
##################

# 5) Construccion de las RUTAS GENERALES del repo.
RUTA_DATA = RUTA_PROYECTO / "data"  # construye la RUTA de la CARPETA data          --> partiendo desde la CARPETA raiz del proyecto, cuya ruta es señalada en la variable RUTA_PROYECTO
RUTA_BRONZE = RUTA_DATA / "bronze"  # construye la RUTA de la CARPETA bronze        --> partiendo desde la CARPETA data, cuya ruta es señalada en la variable RUTA_DATA
RUTA_SILVER = RUTA_DATA / "silver"  # construye la RUTA de la CARPETA silver        --> partiendo desde la CARPETA data, cuya ruta es señalada en la variable RUTA_DATA
RUTA_GOLD = RUTA_DATA / "gold"      # construye la RUTA de la CARPETA gold          --> partiendo desde la CARPETA data, cuya ruta es señalada en la variable RUTA_DATA
RUTA_LOGS = RUTA_PROYECTO / "logs"  # construye la RUTA del ARCHIVO logs      --> partiendo desde la CARPETA raiz del proyecto, cuya ruta es señalada en la variable RUTA_PROYECTO

# 6) Construccion de las RUTAS ESPECÍNFICAS de entrada y salida.
# 6.1 Rutas BRONZE
RUTA_SENSOR_EVENTS_BRONZE = RUTA_BRONZE / "iot" / "sensor_events.csv"       # --> define la ruta del ARCHIVO bronze de eventos de sensores,       --> partiendo desde la CARPETA bronze, cuya ruta es señalada en la variable RUTA_BRONZE
RUTA_ACTUATOR_EVENTS_BRONZE = RUTA_BRONZE / "iot" / "actuator_events.csv"   # --> define la ruta del ARCHIVO bronze de eventos de actuadores,     --> partiendo desde la CARPETA bronze, cuya ruta es señalada en la variable RUTA_BRONZE
RUTA_DEVICES_MASTER_BRONZE = RUTA_BRONZE / "master" / "devices_master.csv"  # --> define la ruta del ARCHIVO bronze del catálogo de dispositivos  --> partiendo desde la CARPETA bronze, cuya ruta es señalada en la variable RUTA_BRONZE
RUTA_ZONES_MASTER_BRONZE = RUTA_BRONZE / "master" / "zones_master.csv"      # --> define la ruta del ARCHIVO bronze del catálogo de zonas,        --> partiendo desde la CARPETA bronze, cuya ruta es señalada en la variable RUTA_BRONZE
RUTA_WEATHER_API_BRONZE = RUTA_BRONZE / "external" / "weather_api" / f"run_date={FECHA_EJECUCION}" / "weather_api_events.json" # --> define la ruta del ARCHIVO bronze del clima externo,  --> partiendo desde la CARPETA bronze, cuya ruta es señalada en la variable RUTA_BRONZE

# 6.2 Rutas SILVER
RUTA_SENSOR_EVENTS_SILVER = RUTA_SILVER / "iot" / "sensor_events"         # --> define la ruta de la CARPETA silver donde se escribirán los eventos de sensores    --> partiendo desde la CARPETA silver
RUTA_ACTUATOR_EVENTS_SILVER = RUTA_SILVER / "iot" / "actuator_events"     # --> define la ruta de la CARPETA silver donde se escribirán los eventos de actuadores  --> partiendo desde la CARPETA silver
RUTA_DEVICES_MASTER_SILVER = RUTA_SILVER / "master" / "devices_master"    # --> define la ruta de la CARPETA silver del catálogo de dispositivos                   --> partiendo desde la CARPETA silver
RUTA_ZONES_MASTER_SILVER = RUTA_SILVER / "master" / "zones_master"        # --> define la ruta de la CARPETA silver del catálogo de zonas                          --> partiendo desde la CARPETA silver
RUTA_WEATHER_API_SILVER = RUTA_SILVER / "external" / "weather_api_events" # --> define la ruta de la CARPETA silver del clima externo                              --> partiendo desde la CARPETA silver

# 7) Agrupamiento de las rutas en DICCIONARIOS para usarlas fácilmente (hace que el resto del proyecto sea más cómodo)
# 7.1 Diccionario de rutas bronze
DATASETS_BRONZE = {  # agrupa todas las rutas bronze en un único diccionario para accederlas fácil
    "sensor_events": RUTA_SENSOR_EVENTS_BRONZE,     # --> guarda la ruta bronze de SENSORES bajo una clave clara        --> "sensor_events"   en este caso.
    "actuator_events": RUTA_ACTUATOR_EVENTS_BRONZE, # --> guarda la ruta bronze de ACTUADORES bajo una clave clara      --> "actuator_events" en este caso.
    "devices_master": RUTA_DEVICES_MASTER_BRONZE,   # --> guarda la ruta bronze de DISPOSITIVOS bajo una clave clara    --> "devices_master"  en este caso.
    "zones_master": RUTA_ZONES_MASTER_BRONZE,       # --> guarda la ruta bronze de ZONAS bajo una clave clara           --> "zones_master"    en este caso.
    "weather_api_events": RUTA_WEATHER_API_BRONZE,  # --> guarda la ruta bronze del CLIMA EXTERNO bajo una clave clara  --> "weather_api_events" en este caso.
}

# 7.2 Diccionario de rutas silver
DATASETS_SILVER = {  # agrupa todas las rutas silver en un único diccionario para acceder a ellos por su nombre
    "sensor_events": RUTA_SENSOR_EVENTS_SILVER,     # --> guarda la ruta silver de sensores bajo una clave clara
    "actuator_events": RUTA_ACTUATOR_EVENTS_SILVER, # --> guarda la ruta silver de actuadores bajo una clave clara
    "devices_master": RUTA_DEVICES_MASTER_SILVER,   # --> guarda la ruta silver de dispositivos bajo una clave clara
    "zones_master": RUTA_ZONES_MASTER_SILVER,       # --> guarda la ruta silver de zonas bajo una clave clara
    "weather_api_events": RUTA_WEATHER_API_SILVER,  # --> guarda la ruta silver del clima externo bajo una clave clara
}


'''
A nivel conceptual, el archivo settings.py es:   
           
        EL MAPA DEL PROYECTO

A nivel técnico, hace estas cosas:
    - importa Path
    - define constantes generales
    - define la configuración básica de Spark
    - descubre la raíz del repo
    - construye rutas generales
    - construye rutas concretas de entrada y salida
    - agrupa las rutas en diccionarios reutilizables


A nivel práctico, le evita al resto del proyecto tener que preguntarse:
    - “¿dónde está este archivo?”
    - “¿a qué carpeta debo escribir?”
    - “¿qué fecha de ejecución se usa?”
    - “¿qué nombre tiene el pipeline?”

Porque todo eso ya queda centralizado acá.



CONCLUYENDO:
    - settings.py no procesa datos
    - settings.py organiza el territorio
    - los otros archivos después usarán ese territorio para:
        leer
        validar
        transformar
        escribir'''