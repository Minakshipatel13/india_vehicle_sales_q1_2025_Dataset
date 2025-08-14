import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

st.title("Random Forest Regression Predictor")

# Example: Assume you need 10 features as input
inputs = []
for i in range(100):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    prediction = model.predict([inputs])
    st.success(f"Predicted Output: {prediction[0]}")