# Predicción de Fraude en Transacciones - Aplicación Streamlit

Esta es una aplicación web desarrollada con **Streamlit** que utiliza un modelo de aprendizaje automático entrenado con **TensorFlow/Keras** para predecir si una transacción es fraudulenta o no. El modelo se basa en diversas características de la transacción, como el monto escalado (`scaled_amount`), el tiempo escalado (`scaled_time`), y otros vectores (`V1`, `V2`, ..., `V28`).

## Descripción

La aplicación permite al usuario ingresar manualmente valores para las columnas `V2`, `V4`, `V11`, y `V19`. El resto de las columnas se completan automáticamente con valores aleatorios. Basado en estos datos, el modelo predice si la transacción es fraudulenta.

### Tecnologías utilizadas:
- **Streamlit**: Para construir la interfaz web.
- **TensorFlow/Keras**: Para cargar y utilizar el modelo de predicción.
- **NumPy**: Para el manejo de arreglos y generación de datos aleatorios.

## Capturas de pantalla

_Inserta aquí capturas de pantalla si tienes, para mostrar cómo se ve la aplicación._

## Estructura del Proyecto

```plaintext
├── models/
│   └── modelo_keras.h5         # Modelo entrenado de Keras
├── app.py                      # Código principal de la aplicación Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

## Instalacion de Requerimientos
```bash
pip install -r requirements.txt
```

## Ejecucion del programa
```bash
streamlit run app.py
```
