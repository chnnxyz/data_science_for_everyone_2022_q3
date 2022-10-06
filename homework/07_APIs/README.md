# Tarea: Apis

En esta tarea, desarrollarás un API en flask que se conecte a otra api para usar
datos.

## Extracción de datos:

Usa las librerías `pandas` y `requests` para acceder a los datos de una api de tu interés, guarda todos los dataframes que necesites como variables globales para tu API. Haz todo el preprocesamiento que necesites. Puedes apoyarte de un Jupyter para tus pruebas.

## Endpoints

Usa diferentes endpoints para predecir con tres de los algoritmos vistos en clase un input que meta el usuario.

Cada endpoint debe entrenar un modelo diferente usando datos provistos por el usuario.

La respuesta de estos endpoints debe incluir:

- El nombre del modelo usado
- El error de entrenamiento
- El número de puntos de datos usados para entrenamiento.
- La predicción del modelo.

Además, crea un endpoint en `/` que contenga la documentación del API en formato HTML.
