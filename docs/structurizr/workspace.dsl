workspace "Telemetria Greenhouse Pipeline" "Modelo C4 refinado del proyecto telemetriaGreenhouse" {

    model {
        operador = person "Operador" "Ejecuta el pipeline batch desde terminal y revisa resultados." {
            tags "Actor"
        }

        sistema = softwareSystem "Telemetria Greenhouse Pipeline" "Pipeline batch en Python + Spark para leer Bronze, validar datasets y persistir Silver." {

            runner = container "CLI Runner" "scripts/run_pipeline.py" "Python" "Bootstrapper que prepara imports y transfiere control a main.py." {
                tags "Arranque"
            }

            app = container "Pipeline Application" "src/greenhouse_pipeline" "Python + PySpark" "Orquesta el ciclo de vida, ejecuta pipelines, lee Bronze, valida y escribe Silver." {
                tags "Orquestacion"

                main = component "main.py" "Crea SparkSession, coordina el ciclo de vida global y llama a ejecutar_todos_los_pipelines(spark)." "Python" {
                    tags "Arranque,Orquestacion"
                }

                settings = component "settings.py" "Centraliza identidad del pipeline, Spark, rutas Bronze/Silver/Logs y política de salida." "Python" {
                    tags "Configuracion"
                }

                pipelines = component "pipelines.py" "Orquesta dataset por dataset: leer, contar, validar, escribir y loguear." "Python" {
                    tags "Orquestacion"
                }

                readers = component "readers.py" "Resuelve ruta + esquema y construye DataFrames desde Bronze." "Python + PySpark" {
                    tags "Ingestion"
                }

                schemas = component "schemas.py" "Declara la estructura esperada de cada dataset mediante StructType/StructField." "Python + PySpark" {
                    tags "Estructura"
                }

                validators = component "validators.py" "Ejecuta la capa de calidad sobre DataFrames." "Python + PySpark" {
                    tags "Calidad"
                }

                quality = component "quality_rules.py" "Declara columnas requeridas, no nulas, catálogos, rangos y claves de duplicados." "Python" {
                    tags "Calidad"
                }

                writers = component "writers.py" "Resuelve rutas Silver y persiste DataFrames en Parquet." "Python + PySpark" {
                    tags "Persistencia"
                }

                logger = component "logger.py" "Configura y expone el logger del proyecto." "Python" {
                    tags "Observabilidad"
                }
            }

            bronze = container "Bronze Data Store" "data/bronze" "File System (CSV/JSON)" "Almacena datasets de entrada: sensor_events, actuator_events, devices_master, zones_master y weather_api_events." {
                tags "Almacenamiento"
            }

            silver = container "Silver Data Store" "data/silver" "File System (Parquet)" "Almacena datasets validados y persistidos en formato analítico." {
                tags "Almacenamiento"
            }

            logs = container "Log Store" "logs/" "File System" "Almacena logs técnicos de ejecución." {
                tags "Observabilidad"
            }

            operador -> runner "Ejecuta desde terminal"
            runner -> app "Invoca main()"
            app -> bronze "Lee datasets Bronze"
            app -> silver "Escribe datasets Silver"
            app -> logs "Escribe logs"

            runner -> main "Importa y ejecuta main()"

            main -> settings "Usa configuración de Spark e identidad"
            main -> logger "Obtiene logger"
            main -> pipelines "Invoca lote completo"

            pipelines -> logger "Registra ejecución"
            pipelines -> readers "Lee dataset Bronze"
            pipelines -> validators "Valida DataFrame"
            pipelines -> writers "Escribe dataset Silver"

            readers -> settings "Consulta DATASETS_BRONZE"
            readers -> schemas "Consulta ESQUEMAS"
            readers -> bronze "Lee CSV/JSON"

            validators -> quality "Consulta REGLAS_CALIDAD"

            writers -> settings "Consulta DATASETS_SILVER y política de salida"
            writers -> silver "Escribe Parquet"

            logger -> logs "Escribe logs"
        }
    }

    views {
        systemContext sistema "system-context" {
            include *
            autoLayout lr
            title "System Context - Telemetria Greenhouse Pipeline"
        }

        container sistema "containers" {
            include *
            autoLayout lr
            title "Container View - Telemetria Greenhouse Pipeline"
        }

        component app "components" {
            include *
            autoLayout lr
            title "Component View - Pipeline Application"
        }

        dynamic app "sensor-events-flow" {
            title "Dynamic View - sensor_events end-to-end flow"
            description "Secuencia principal del flujo extremo a extremo de sensor_events."

            1: operador -> runner "Ejecuta scripts/run_pipeline.py"
            2: runner -> main "Importa y ejecuta main()"
            3: main -> logger "Obtiene logger"
            4: main -> settings "Lee SPARK_APP_NAME y SPARK_MASTER"
            5: main -> pipelines "ejecutar_todos_los_pipelines(spark)"
            6: pipelines -> logger "Inicia procesamiento de sensor_events"
            7: pipelines -> readers "leer_dataset_bronze(spark, sensor_events)"
            8: readers -> settings "Obtiene ruta Bronze"
            9: readers -> schemas "Obtiene ESQUEMA_SENSOR_EVENTS"
            10: readers -> bronze "Lee sensor_events.csv como DataFrame"
            11: pipelines -> logger "Registra cantidad de filas"
            12: pipelines -> validators "ejecutar_validaciones_dataset(df, sensor_events)"
            13: validators -> quality "Obtiene REGLAS_CALIDAD[sensor_events]"
            14: pipelines -> writers "escribir_dataset_silver(df, sensor_events)"
            15: writers -> settings "Obtiene ruta Silver y modo/formato"
            16: writers -> silver "Escribe Parquet en Silver"
            17: pipelines -> logger "Registra cierre de sensor_events"

            autoLayout lr
        }

        styles {
            element "Person" {
                shape Person
                background #08427b
                color #ffffff
            }

            element "Software System" {
                background #1168bd
                color #ffffff
            }

            element "Container" {
                background #438dd5
                color #ffffff
            }

            element "Component" {
                background #85bbf0
                color #000000
            }

            element "Actor" {
                background #08427b
                color #ffffff
            }

            element "Arranque" {
                background #d9edf7
                color #000000
            }

            element "Configuracion" {
                background #fcf8e3
                color #000000
            }

            element "Estructura" {
                background #f5e8ff
                color #000000
            }

            element "Ingestion" {
                background #dff0d8
                color #000000
            }

            element "Calidad" {
                background #f2dede
                color #000000
            }

            element "Persistencia" {
                background #e8f5e9
                color #000000
            }

            element "Observabilidad" {
                background #eeeeee
                color #000000
            }

            element "Almacenamiento" {
                background #f9f9f9
                color #000000
            }
        }

        theme default
    }
}
