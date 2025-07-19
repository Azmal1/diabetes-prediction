import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("diabetes_model.pkl")

# Title
st.title("🩺 Diabetes Prediction App")
st.markdown("Enter patient health data to check for diabetes risk.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    result = model.predict(input_data)[0]
    if result == 1:
        st.error("🔴 The patient is likely to have diabetes.")
    else:
        st.success("🟢 The patient is not likely to have diabetes.")
