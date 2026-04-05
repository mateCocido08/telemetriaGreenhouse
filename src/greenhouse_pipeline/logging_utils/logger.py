import logging                                          # importa la librería estándar de Python para REGISTRAR MENSAJES del sistema
from pathlib import Path                                        # importa Path para trabajar con RUTAS de "archivos y carpetas"
from greenhouse_pipeline.config.settings import RUTA_LOGS       # importa RUTA_LOGS para saber donde se guardarán los "logs"
from greenhouse_pipeline.config.settings import NOMBRE_PIPELINE # importa NOMBRE_PIPELINE para saber como nombrar el logger

def obtener_logger() -> logging.Logger:                         # define una función que crea y devuelve un logger reutilizable
    RUTA_LOGS.mkdir(parents=True, exist_ok=True)                # crea la carpeta de logs si no existe y evita error si ya existe

    logger = logging.getLogger(NOMBRE_PIPELINE)                 # obtiene o crea un logger identificado con el nombre del pipeline

    if logger.handlers:                                         # verifica si el logger ya tiene handlers agregados previamente
        return logger                                           # devuelve el logger existente para no duplicar salidas

    logger.setLevel(logging.INFO)                               # define el nivel mínimo de mensajes que se registrarán

    ruta_archivo_log = RUTA_LOGS / "pipeline.log"               # construye la ruta completa del archivo de log principal

    formato = logging.Formatter(                                # crea el formato visual que tendrán los mensajes de log
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"  # define fecha, nivel, nombre del logger y mensaje
    )  

    handler_consola = logging.StreamHandler()   # crea un handler para mostrar logs en consola
    handler_consola.setFormatter(formato)       # aplica el formato definido a la salida de consola

    handler_archivo = logging.FileHandler(ruta_archivo_log, encoding="utf-8")   # crea un handler para escribir logs en archivo
    handler_archivo.setFormatter(formato)                                       # aplica el formato definido a la salida en archivo

    logger.addHandler(handler_consola)          # conecta el handler de consola al logger
    logger.addHandler(handler_archivo)          # conecta el handler de archivo al logger

    logger.propagate = False            # evita que el mensaje suba al logger raíz y se duplique en pantalla

    return logger                       # devuelve el logger ya configurado para ser usado por el resto del proyecto