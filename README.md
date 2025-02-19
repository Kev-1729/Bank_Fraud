# Fraud Detection in Transactions - Streamlit Application  

This is a web application developed with **Streamlit** that uses a machine learning model trained with **TensorFlow/Keras** to predict whether a transaction is fraudulent or not. The model is based on various transaction features, such as the scaled amount (`scaled_amount`), scaled time (`scaled_time`), and other vectors (`V1`, `V2`, ..., `V28`).  

## Description  

The application allows users to manually enter values for the columns `V2`, `V4`, `V11`, and `V19`. The remaining columns are automatically filled with random values. Based on this data, the model predicts whether the transaction is fraudulent.  

### Technologies Used:  
- **Streamlit**: To build the web interface.  
- **TensorFlow/Keras**: To load and use the prediction model.  
- **NumPy**: For handling arrays and generating random data.  

## Screenshots  

_Insert screenshots here to showcase the application._  

## Project Structure  

```plaintext
├── models/
│   └── modelo_keras.h5         # Trained Keras model  
├── app.py                      # Main Streamlit application code  
├── requirements.txt            # Project dependencies  
└── README.md                   # This file  
```  

## Install Requirements  
```bash
pip install -r requirements.txt
```  

## Run the Application  
```bash
streamlit run app.py
```  
