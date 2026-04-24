from statsmodels.tsa.base import prediction
from sqlalchemy import Transaction
import streamlit as st
import pandas as pd 
import numpy as np
import joblib
import sklearn 
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

model  = joblib.load("fraud_detection_pipeline.pkl")    

st.title("Fraud Detection System")
    

st.markdown("""
## About
This is a fraud detection system using machine learning.
""")    
st.divider()

tranaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])

amount = st.number_input("Amount",min_value=0.0,value = 1000.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)",min_value=0.0,value = 1000.0)
newbalanceOrig = st.number_input("New Balance (Sender)",min_value=0.0,value = 5000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)",min_value=0.0,value = 0.0)
newbalanceDest = st.number_input("New Balance (Receiver)",min_value=0.0,value = 0.0)


if st.button("Predict"):
    input_data = {
        'type' : tranaction_type,
        'amount' : amount,
        'oldbalanceOrg' : oldbalanceOrg,
        'newbalanceOrig' : newbalanceOrig,
        'oldbalanceDest' : oldbalanceDest,
        'newbalanceDest' : newbalanceDest
    }   

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.subheader(f"Prediction : ' {int(prediction)}' ")

    if prediction == 1:
        st.error("This transaction is fraudulent !")
    else:
        st.success("This transaction is not fraudulent")