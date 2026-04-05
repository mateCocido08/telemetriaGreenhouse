# Arquitectura del proyecto

## Resumen

`telemetriaGreenhouse` es un proyecto de portfolio orientado a ingeniería de datos que toma como contexto un dominio IoT de monitoreo y control de un vivero/invernadero, y reconstruye su capa de datos como un pipeline batch en Python + PySpark.

La arquitectura actual sigue una lógica Bronze → Silver:

- **Bronze**: fuentes crudas de entrada
- **Silver**: datasets leídos con esquema explícito, validados y persistidos en formato analítico

El objetivo de esta arquitectura no es simular una plataforma productiva completa, sino mostrar criterio técnico en organización de código, modelado del dato, validación y trazabilidad.

## Punto de partida del flujo

La ejecución comienza en:

- `scripts/run_pipeline.py`

Ese script resuelve la raíz del proyecto, agrega `src` al `sys.path` y luego importa y ejecuta `main()`. Su función es actuar como punto de entrada operativo del pipeline.

## Orquestación global

La función principal vive en:

- `main.py`

Su responsabilidad es:

- obtener el logger del proyecto
- crear la `SparkSession`
- ejecutar el lote completo de pipelines
- registrar inicio, éxito, errores y cierre
- detener la `SparkSession` al final

Esto convierte a `main.py` en el coordinador del ciclo de vida general de la aplicación.

## Configuración central

La configuración está centralizada en:

- `settings.py`

Este módulo concentra:

- nombre del pipeline
- fecha de ejecución
- modo de escritura
- formato de salida
- configuración base de Spark
- rutas generales del proyecto
- rutas específicas Bronze y Silver
- diccionarios de acceso por nombre de dataset

Desde el punto de vista conceptual, `settings.py` funciona como el mapa del territorio del proyecto.

## Modelo de datasets

La estructura esperada de los datos está definida en:

- `schemas.py`

Allí se declaran explícitamente los esquemas de:

- `sensor_events`
- `actuator_events`
- `devices_master`
- `zones_master`
- `weather_api_events`

Esto permite que la lectura no dependa de inferencias automáticas de tipos y que cada dataset tenga una forma esperada claramente definida.

## Calidad del dato

La capa de calidad está dividida en dos partes:

### 1. Reglas declarativas
- `quality_rules.py`

Este archivo define, por dataset:

- columnas requeridas
- columnas no nulas
- valores permitidos
- rangos numéricos
- claves naturales para detección de duplicados

### 2. Ejecución de validaciones
- `validators.py`

Este módulo toma un `DataFrame` y aplica las reglas correspondientes. Entre las validaciones implementadas se encuentran:

- dataset no vacío
- presencia de columnas obligatorias
- ausencia de nulos en columnas críticas
- catálogos de valores permitidos
- rangos numéricos razonables
- duplicados según clave natural

La separación entre `schemas.py` y `quality_rules.py` es una de las decisiones más importantes del proyecto: una cosa es la **forma esperada** del dato y otra distinta es su **aceptabilidad de negocio/técnica**.

## Lectura de datos

La lectura está implementada en:

- `readers.py`

Este módulo:

- resuelve la ruta Bronze del dataset
- obtiene su esquema
- decide si leer CSV o JSON
- devuelve un `DataFrame` listo para ser procesado

En esta versión del proyecto:

- la mayoría de los datasets se leen como CSV
- `weather_api_events` se lee como JSON

## Escritura de datos

La salida está implementada en:

- `writers.py`

Su responsabilidad es:

- resolver la ruta Silver correspondiente
- asegurar la existencia de la carpeta de salida
- escribir el `DataFrame` en el formato configurado

Actualmente, el proyecto escribe en:

- **Parquet**
- modo **overwrite**

Esto materializa una capa Silver simple pero clara, orientada a reutilización analítica.

## Orquestación por dataset

La lógica de procesamiento vive en:

- `pipelines.py`

Este módulo define una función general para procesar datasets desde Bronze a Silver, siguiendo este patrón:

1. leer
2. contar registros
3. validar
4. escribir
5. registrar en logs

Además, contiene funciones específicas para cada dataset y una función que ejecuta el lote completo en un orden controlado.

## Observabilidad

La trazabilidad técnica está dada por:

- `logger.py`

Este módulo configura un logger reutilizable que:

- escribe en consola
- escribe en archivo
- usa formato uniforme
- evita duplicación de handlers

Gracias a esto, el proyecto puede registrar el inicio y cierre de la aplicación, la creación de Spark, el procesamiento de cada dataset y cualquier error que ocurra durante la ejecución.

## Flujo resumido

De forma resumida, el flujo del proyecto es el siguiente:

1. `run_pipeline.py` inicia la ejecución
2. `main.py` crea la `SparkSession`
3. `pipelines.py` recorre los datasets
4. `readers.py` lee Bronze aplicando esquema
5. `validators.py` ejecuta reglas de calidad
6. `writers.py` persiste el resultado en Silver
7. `logger.py` deja trazabilidad de todo el proceso

## Decisiones técnicas visibles en esta versión

### Separación de responsabilidades
Cada módulo tiene un rol claro: configuración, modelado, lectura, validación, escritura, logging y orquestación.

### Esquema explícito
La lectura usa esquemas definidos manualmente, evitando depender de inferencias automáticas.

### Calidad desacoplada
Las reglas de calidad no están mezcladas con la lectura ni con la escritura.

### Persistencia analítica simple
La salida en Parquet representa una capa Silver compacta, razonable y reutilizable.

### Spark mínimo viable
El proyecto usa un subconjunto concreto de Spark, suficiente para comprender el pipeline sin complejidad innecesaria.

## Alcance actual

Este repositorio no busca presentar una plataforma IoT productiva completa ni una solución de datos cerrada. Su valor actual está en mostrar:

- comprensión del dominio
- modelado de datasets
- organización modular
- validación explícita del dato
- trazabilidad del flujo
- capacidad de documentación técnica

En ese sentido, el proyecto funciona como una base de portfolio bien estructurada y abierta a evolución futura.