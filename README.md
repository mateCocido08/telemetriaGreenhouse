# telemetriaGreenhouse

Proyecto de portfolio orientado a ingeniería de datos, construido a partir del contexto técnico de un trabajo final de diplomatura en IoT presentado en UTN en 2023.

## Idea del proyecto

Este repositorio toma como punto de partida un proyecto académico de monitoreo y control remoto de un vivero/invernadero, basado en sensores, actuadores, ESP32, Raspberry Pi, MQTT, Mosquitto, Node-RED y Blynk. A partir de ese contexto, el proyecto reconstruye la capa de datos desde una perspectiva de ingeniería de datos: modelado de datasets, lectura con esquema explícito, validaciones de calidad y persistencia analítica.

El foco del repositorio no está en presentar una solución productiva cerrada, sino en mostrar criterio técnico, organización modular y capacidad de evolución desde IoT hacia Data Engineering.

## Qué muestra este repositorio

- organización de un pipeline batch en Python + PySpark
- separación entre configuración, lectura, validación, escritura y orquestación
- definición explícita de esquemas por dataset
- reglas de calidad desacopladas de la lectura
- persistencia en formato Parquet sobre una capa Silver
- documentación arquitectónica y modelado visual del sistema

## Contexto de origen

El trabajo académico original se centró en optimizar la gestión y producción de brotes de semillas en un vivero, mediante monitoreo de temperatura, humedad, luminosidad y humedad del suelo, y control remoto de actuadores como válvula de riego, inyector y extractor de aire.

Arquitectura base del proyecto original:

- sensores en vivero: DHT22, TSL2561 y sensor capacitivo de humedad de suelo
- ESP32 como cliente MQTT
- Raspberry Pi 4 con Mosquitto y Node-RED
- visualización y control remoto con Blynk

En este repositorio, ese contexto se traduce a una capa de datos que modela eventos de sensores, eventos de actuadores, catálogos maestros y una fuente externa meteorológica.

Más detalle: [Contexto UTN 2023](docs/contexto-utn.md)

## Arquitectura de datos del repositorio

El pipeline actual trabaja con una arquitectura Bronze → Silver.

Datasets modelados:

- `sensor_events`
- `actuator_events`
- `devices_master`
- `zones_master`
- `weather_api_events`

Componentes principales:

- `scripts/run_pipeline.py`: punto de entrada manual
- `main.py`: crea la SparkSession y orquesta la ejecución global
- `settings.py`: centraliza rutas, parámetros y configuración base
- `schemas.py`: define la estructura esperada de cada dataset
- `quality_rules.py`: define reglas de calidad por dataset
- `readers.py`: lectura de fuentes Bronze
- `validators.py`: validación de DataFrames
- `writers.py`: escritura en Silver
- `pipelines.py`: orquestación dataset por dataset
- `logger.py`: trazabilidad técnica de ejecución

## Flujo general

1. `run_pipeline.py` inicia la ejecución
2. `main.py` crea la `SparkSession`
3. `pipelines.py` procesa cada dataset
4. `readers.py` lee Bronze aplicando esquema explícito
5. `validators.py` ejecuta reglas de calidad
6. `writers.py` persiste resultados en Silver
7. `logger.py` registra el flujo completo

## Qué busco demostrar con este proyecto

- capacidad de modelar un dominio técnico en datasets claros
- criterio para separar estructura del dato y reglas de calidad
- comprensión del flujo de un pipeline batch en Spark
- capacidad para documentar arquitectura, ejecución y decisiones técnicas
- evolución de un proyecto IoT hacia una base de ingeniería de datos

## Estado del proyecto

Estado actual: versión de portfolio/documentación técnica.

Próximos pasos previstos:

- seguir mejorando la documentación
- enriquecer diagramas y vistas arquitectónicas
- evolucionar la solución hacia una implementación más cercana a un caso real
- actualizar el repositorio a medida que el proyecto avance en la práctica

## Documentación

- [Contexto UTN 2023](docs/contexto-utn.md)
- [Modelo C4 / Structurizr / modelo_C4_structurizr.md](docs/modelo_C4_structurizr.md)

## Nota

Este repositorio no se presenta como una solución productiva final, sino como una base técnica bien estructurada para mostrar diseño de pipelines, modelado del dato, validación y documentación aplicada a un dominio IoT realista.