"""
Punto de entrada operativo del proyecto.

Este script resuelve la raíz del repositorio, expone `src` en `sys.path`
e invoca `greenhouse_pipeline.main`.
"""

from pathlib import Path
import sys

RUTA_SCRIPT = Path(__file__).resolve()
RUTA_PROYECTO = RUTA_SCRIPT.parents[1]
RUTA_SRC = RUTA_PROYECTO / "src"

if str(RUTA_SRC) not in sys.path:
    sys.path.insert(0, str(RUTA_SRC))

from greenhouse_pipeline.main import main


if __name__ == "__main__":
    main()
