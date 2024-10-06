import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

# Ruta del modelo preentrenado
MODEL_PATH = 'models/modelo_keras.h5'

# Cargar el modelo solo una vez utilizando el nuevo st.cache_resource
@st.cache_resource
def load_my_model():
    model = load_model(MODEL_PATH)
    return model

# Función para realizar la predicción
def model_prediction(input_data, model):
    # Convertir los datos de entrada en un array numpy y asegurarse de que tienen el formato correcto
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

# Cargar el modelo
model = load_my_model()

# Título y descripción
st.title("Predicción de Transacciones con Modelo de Keras")
st.markdown("""
### Ingresar valores de las características:
Este modelo predice si una transacción es fraudulenta o no basada en las características de la transacción, tales como `scaled_amount`, `scaled_time`, y varias otras características (`V1`, `V2`, ... `V28`).
Por favor, ingresa los valores solo para `V2`, `V4`, `V11`, y `V19`. El resto de las características se llenarán con valores aleatorios.
""")

# Nombres de todas las columnas
columnas = ['scaled_amount', 'scaled_time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8',
            'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

# Columnas que el usuario ingresa manualmente
input_columns = ['V2', 'V4', 'V11', 'V19']

# Generar valores aleatorios por defecto para todas las columnas
input_data = []
for col in columnas:
    if col in input_columns:
        # Pedir al usuario que ingrese valores solo para V2, V4, V11, y V19
        value = st.number_input(f'Característica {col}', min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
    else:
        # Generar un valor aleatorio para el resto de las columnas
        value = np.random.uniform(-10.0, 10.0)
    input_data.append(value)

# Botón para realizar la predicción
if st.button("Realizar predicción"):
    # Llamar a la función de predicción con los datos ingresados
    prediction = model_prediction(input_data, model)
    
    # Mostrar el resultado
    st.subheader("Resultado de la Predicción:")
    st.write(f"La predicción del modelo es: {'Fraude' if prediction[0][0] > 0.5 else 'No Fraude'}")
    
# Pie de página
st.markdown("""
---
Aplicación creada por Kevin Tupac Agüero. Esta aplicación utiliza un modelo de aprendizaje automático para detectar fraudes en transacciones basadas en características específicas.
""")
