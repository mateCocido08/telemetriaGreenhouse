import logging

from greenhouse_pipeline.config.settings import NOMBRE_PIPELINE, RUTA_LOGS


def obtener_logger() -> logging.Logger:
    """Devuelve un logger reutilizable para todo el proyecto."""
    RUTA_LOGS.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(NOMBRE_PIPELINE)

    # Evita duplicar handlers cuando el logger ya fue configurado.
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    ruta_archivo_log = RUTA_LOGS / "pipeline.log"
    formato = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    handler_consola = logging.StreamHandler()
    handler_consola.setFormatter(formato)

    handler_archivo = logging.FileHandler(ruta_archivo_log, encoding="utf-8")
    handler_archivo.setFormatter(formato)

    logger.addHandler(handler_consola)
    logger.addHandler(handler_archivo)

    logger.propagate = False

    return logger
