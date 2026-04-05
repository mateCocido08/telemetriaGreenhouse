#!/usr/bin/env bash
set -euo pipefail

CONTAINER_NAME="structurizr-lite"
HOST_PORT="8080"
CONTAINER_PORT="8080"
WORKSPACE_DIR="/media/andres/sdb5/1 - Work Space (SSD 240G)/proj_github/telemetriaGreenhouse/docs/structurizr"
WORKSPACE_FILE="${WORKSPACE_DIR}/workspace.dsl"
IMAGE="structurizr/lite"

echo "Verificando archivo workspace.dsl..."
if [[ ! -f "$WORKSPACE_FILE" ]]; then
    echo "ERROR: No existe el archivo:"
    echo "  $WORKSPACE_FILE"
    exit 1
fi

echo "Descargando/actualizando imagen ${IMAGE}..."
docker pull "$IMAGE"

echo "Eliminando contenedor previo si existe..."
docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

echo "Levantando contenedor ${CONTAINER_NAME} en segundo plano..."
docker run -d \
  --name "$CONTAINER_NAME" \
  -p "${HOST_PORT}:${CONTAINER_PORT}" \
  -v "${WORKSPACE_DIR}:/usr/local/structurizr" \
  "$IMAGE"

echo
echo "Contenedor levantado."
echo "Abre en el navegador:"
echo "  http://localhost:${HOST_PORT}"
echo
echo "Para verificar:"
echo "  docker ps --format \"table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\""
echo
echo "Para ver logs:"
echo "  docker logs -f ${CONTAINER_NAME}"
