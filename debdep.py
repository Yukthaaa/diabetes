# -*- coding: utf-8 -*-
"""DebDep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vn1FBXkJIJ1u7OSkO6Ip19B_C5EMAs67
"""

import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load your XGBoost model (replace 'modelXGB.pkl' with your model file)
with open("modelXGB.pkl", "rb") as file:
    modelXGB = pickle.load(file)

# Streamlit app
st.title("Patient Readmission Risk Prediction")
st.markdown("By TEAM 1")

# Load an image for the app
image = Image.open("diabetes.jpg")
st.image(image, use_column_width=True)

# Input fields for user to enter patient attributes
st.subheader("Enter Patient Information:")
num_lab_procedures = st.number_input("Number of Lab Procedures", min_value=0, max_value=100, value=0)
diag_1 = st.text_input("Primary Diagnosis (diag_1)", "")
diag_2 = st.text_input("Secondary Diagnosis (diag_2)", "")
num_medications = st.number_input("Number of Medications", min_value=0, max_value=50, value=0)
diag_3 = st.text_input("Tertiary Diagnosis (diag_3)", "")
time_in_hospital = st.number_input("Time in Hospital (days)", min_value=0, max_value=365, value=0)
number_inpatient = st.number_input("Number of Inpatient Visits", min_value=0, max_value=20, value=0)
age = st.number_input("Age", min_value=0, max_value=150, value=0)

# Predict button
if st.button("Predict Risk"):
    # Create a DataFrame from user inputs
    user_data = pd.DataFrame({
        'num_lab_procedures': [num_lab_procedures],
        'diag_1': [diag_1],
        'diag_2': [diag_2],
        'num_medications': [num_medications],
        'diag_3': [diag_3],
        'time_in_hospital': [time_in_hospital],
        'number_inpatient': [number_inpatient],
        'age': [age]
    })

    categorical_columns = ['age','diag_1', 'diag_2', 'diag_3']  # List of categorical columns
    for column in categorical_columns:
        user_data[column] = label_encoder.transform(user_data[column])


    # Make predictions on user data
    y_probabilities = modelXGB.predict_proba(user_data)[:, 1]

    # Determine the risk bucket based on the predicted probability
    if y_probabilities > 0.7:
        risk_bucket = "High risk"
    elif y_probabilities > 0.3:
        risk_bucket = "Medium risk"
    else:
        risk_bucket = "Low risk"

    # Display the prediction result
    st.header("Risk Prediction:")
    st.subheader(f"The patient is at {risk_bucket} of Readmission.")







