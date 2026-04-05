from pathlib import Path  # Aquí Python carga la herramienta con la que el script podrá calcular rutas de manera robusta.
import sys  # importa sys para poder modificar temporalmente las rutas donde Python busca módulos. Esto habilita el acceso a sys.path, es decir, a la lista de rutas donde Python buscará módulos al resolver imports. 

# Fase 2. run_pipeline.py descubre dónde está parado dentro del repositorio
RUTA_SCRIPT = Path(__file__).resolve()  # Calcula la ruta real del script.  Obtiene la ruta absoluta real de este archivo run_pipeline.py. Ahora el script sabe exactamente dónde está ubicado en el sistema de archivos.
RUTA_PROYECTO = RUTA_SCRIPT.parents[1]  # Calcula la raíz del proyecto.     Con esto el script sube desde su propia ubicación "sripts/" hasta la raíz del repo.
RUTA_SRC = RUTA_PROYECTO / "src"        # Construye la ruta a src.          construye la ruta completa a la carpeta src donde vive el paquete greenhouse_pipeline

# Fase 3. run_pipeline.py modifica el entorno de importación
if str(RUTA_SRC) not in sys.path:  # verifica si la carpeta src ya está incluida en las rutas de búsqueda de Python
    sys.path.insert(0, str(RUTA_SRC))  # agrega src al inicio del path para que Python pueda importar el paquete del proyecto

# Fase 4. Se importa main desde greenhouse_pipeline.main
from greenhouse_pipeline.main import main  # importa la función principal de la aplicación una vez que src ya es visible para Python
    # aquí empieza una fase muy importante, el sistema entra en una subfase de importación encadenada.
        # Fase 4.1. Python entra en main.py              Cuando Python abre main.py, ejecuta primero todo su código de nivel superior.
                    # 8. Importa SparkSession 
                    # 9. Importa parámetros desde settings.py              
        # Fase 4.2. Python ejecuta settings.py
            # settings.py se ejecuta completo de arriba hacia abajo en el momento del import.
                    # 10. Se importa Path
                    # 11. Se definen constantes de identidad general
                    # 12. Se definen parámetros base de Spark
                    # 13. Se calcula RUTA_PROYECTO
                    # 14. Se construyen rutas generales
                    # 15. Se construyen rutas específicas de datasets
                    # 16. Se agrupan esas rutas en diccionarios     
        # Fase 4.3. main.py sigue cargando módulos
            # Después del import de settings, main.py continúa.
                    # 17. Importa obtener_logger desde logger.py
                    # 18. main.py importa ejecutar_todos_los_pipelines desde pipelines.py
        # Fase 4.4. Durante el import de pipelines.py ocurre un efecto importante
        # Fase 4.5. main.py termina de cargarse

# Fase 5. Vuelta a run_pipeline.py
if __name__ == "__main__":  # verifica si este archivo fue ejecutado directamente desde la terminal
    main()  # llama a la función principal del proyecto para iniciar toda la ejecución del pipeline
    

                                        # Fase 6. Comienza la ejecución de main()
                                        # Fase 7. main() crea la SparkSession
                                        # Fase 8. main() transfiere el control a la orquestación de pipelines
                                        
                                        
'''
Síntesis del flujo exacto del tramo 1

Si lo condensamos al máximo, pero sin perder precisión, el flujo real es este:

1 - El usuario ejecuta python scripts/run_pipeline.py.
2 - run_pipeline.py importa Path y sys.
3 - Calcula su propia ruta, la raíz del repo y la ruta src.
4 - Inserta src en sys.path.
5 - Importa main desde greenhouse_pipeline.main.
6 - Durante ese import, Python ejecuta main.py.
7 - main.py importa settings.py, y settings.py carga en memoria:
        - nombre del pipeline,
        - fecha,
        - configuración Spark,
        - rutas generales y específicas,
        - diccionarios Bronze/Silver.
8 - main.py importa logger.py, que define obtener_logger().
9 - main.py importa pipelines.py.
10 - Durante el import de pipelines.py, se ejecuta logger = obtener_logger(), quedando inicializado el logger del proyecto.
11 - main.py termina de definir crear_spark_session() y main().
12 - El control vuelve a run_pipeline.py.
13 - run_pipeline.py entra en su bloque if __name__ == "__main__":.
14 - Llama a main().
15 - main() vuelve a pedir el logger, pero reutiliza el ya existente.
16 - main() registra el inicio del pipeline.
17 - main() crea la SparkSession usando parámetros de settings.py.
18 - main() registra que Spark fue creada correctamente.
19 - main() llama a ejecutar_todos_los_pipelines(spark).
'''