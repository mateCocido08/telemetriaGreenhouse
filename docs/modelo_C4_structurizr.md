# Ver arquitectura con Structurizr

Este proyecto incluye un modelo C4 definido en Structurizr DSL.

## Qué vistas incluye este proyecto

Archivo principal:
- `docs/structurizr/workspace.dsl`

El workspace actual incluye:

- System Context
- Container View
- Component View
- Dynamic View de sensor_events

## Requisito previo

Tener Docker instalado.

## Cómo levantar Structurizr local

Desde la raíz del repositorio, ejecutar:

```bash
docker run -it --rm \
  --name structurizr-local \
  -p 8080:8080 \
  -v "$(pwd)/docs/structurizr:/usr/local/structurizr" \
  structurizr/structurizr local
  ```


## Cómo abrir la interfaz web

Una vez levantado el contenedor, abre en tu navegador:

`http://localhost:8080`

Si todo salió bien, verás las vistas arquitectónicas definidas en el workspace.




## Flujo recomendado de uso
1. abre una terminal en la raíz del repositorio
2. ejecuta el contenedor con el comando indicado
3. abre http://localhost:8080
4. explora las vistas

