# Contexto UTN 2023

## Origen del dominio

Este repositorio toma como punto de partida el trabajo final presentado en 2023 en el marco de la Diplomatura en Internet of Things de UTN.

El problema planteado en ese trabajo consistía en mejorar la gestión y producción de brotes de semillas en un vivero ubicado en el patio trasero de una casa de campo, mediante monitoreo y control más eficiente de las condiciones ambientales y del suelo.

## Solución académica original

La solución propuesta en el trabajo final consistía en escalar una solución previa mediante:

- uso del protocolo MQTT
- servicio Mosquitto como broker
- incorporación de una Raspberry Pi
- uso de Node-RED para procesamiento y análisis
- uso de Blynk para visualización y control remoto

## Hardware principal

La arquitectura original contemplaba:

- **ESP32 Devkit V1** en el vivero, como cliente MQTT
- **Raspberry Pi 4** como broker MQTT con Mosquitto y soporte para Node-RED
- **extensor de rango WiFi**
- **router y modem**
- conectividad WiFi y Ethernet según el tramo de la red

## Sensores y actuadores del dominio

### Sensores
- DHT22 para temperatura y humedad
- TSL2561 para luminosidad
- Capacitive Soil Moisture Sensor V1.2 para humedad del suelo

### Actuadores
- válvula solenoide para riego, controlada por relé
- inyector de aire, controlado por relé
- extractor de aire, controlado por relé

## Flujo funcional original

En el trabajo UTN, los sensores capturaban datos del vivero y el ESP32 los publicaba en tópicos MQTT. La Raspberry Pi, actuando como broker MQTT con Mosquitto, recibía esos datos y los canalizaba hacia Node-RED para procesamiento y análisis. Luego, Blynk permitía al usuario monitorear datos y activar actuadores desde el teléfono móvil.

En el ejemplo de temperatura descrito en el trabajo, el sensor DHT22 generaba el valor, el ESP32 lo publicaba en un tópico MQTT, la Raspberry Pi lo recibía, Node-RED lo procesaba y la aplicación Blynk actualizaba la visualización en el teléfono. De manera equivalente, una acción de control desde el móvil podía llegar por MQTT hasta el ESP32 y activar físicamente una válvula o motor.

## Qué hace este repositorio con ese contexto

Este repositorio no intenta replicar toda la solución IoT de punta a punta, sino **formalizar su capa de datos** desde una perspectiva de ingeniería de datos.

La reinterpretación realizada aquí consiste en modelar y procesar datasets representativos del dominio:

- `sensor_events`
- `actuator_events`
- `devices_master`
- `zones_master`
- `weather_api_events`

## Traducción del dominio IoT a datasets

### `sensor_events`
Representa mediciones generadas por sensores del vivero, como temperatura ambiente, humedad ambiente, humedad de suelo e intensidad lumínica.

### `actuator_events`
Representa comandos y estados de ejecución asociados a actuadores, como válvulas de riego o mecanismos de ventilación.

### `devices_master`
Funciona como catálogo técnico de dispositivos del sistema.

### `zones_master`
Funciona como catálogo espacial/lógico de zonas del invernadero o vivero.

### `weather_api_events`
Agrega una fuente externa de contexto para enriquecer la lectura del entorno.

## Enfoque de ingeniería de datos adoptado

A partir de ese dominio, el proyecto actual se concentra en:

- modelado explícito de esquemas
- centralización de configuración
- lectura controlada desde Bronze
- validaciones de calidad desacopladas
- persistencia en Silver en formato Parquet
- trazabilidad mediante logs

## Valor del proyecto actual

El valor de este repositorio está en mostrar la transición entre dos capas de conocimiento:

1. una capa **IoT / telecomunicaciones / mensajería**
2. una capa **ingeniería de datos / modelado / calidad / persistencia analítica**

Por eso, este repositorio debe leerse como una evolución técnica de un dominio trabajado previamente en la diplomatura, no como un producto cerrado ni como una solución productiva final.