import streamlit as st
import joblib
import numpy as np
from utils import classify_stage

# Load model
model = joblib.load("ef_model.pkl")

st.set_page_config(page_title="CAD Stage Predictor", layout="centered")
st.title("🫀 Coronary Artery Disease Stage Predictor")

st.markdown("Enter the following details to predict Ejection Fraction and CAD stage:")

age = st.number_input("Age", min_value=30, max_value=90, value=50)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=60, max_value=120, value=80)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=160, value=72)
ldl = st.number_input("LDL Cholesterol (mg/dL)", min_value=50, max_value=250, value=100)
troponin_i = st.number_input("Troponin I (ng/mL)", min_value=0.0, max_value=10.0, value=0.01, format="%.2f")

if st.button("Predict"):
    features = np.array([[age, systolic_bp, diastolic_bp, heart_rate, ldl, troponin_i]])
    ef = model.predict(features)[0]
    stage = classify_stage(ef)

    st.subheader("🧾 Results")
    st.write(f"**Predicted Ejection Fraction:** {ef:.2f}%")
    st.write(f"**CAD Stage:** `{stage}`")
