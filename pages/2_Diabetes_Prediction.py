import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Diabetes Prediction", page_icon="🧪", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

.main-card{
background: linear-gradient(135deg,#36d1dc,#5b86e5);
padding:30px;
border-radius:15px;
color:white;
box-shadow:0px 6px 20px rgba(0,0,0,0.25);
}

.result-success{
background:#e6ffed;
padding:20px;
border-radius:12px;
border-left:6px solid #28a745;
font-size:18px;
}

.result-danger{
background:#ffe6e6;
padding:20px;
border-radius:12px;
border-left:6px solid #ff4b4b;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ LOAD MODEL ------------------
model_path = Path(__file__).resolve().parents[1] / "models" / "diabetes_model.pkl"
model = joblib.load(model_path)

# ------------------ HEADER ------------------
st.markdown("""
<div class="main-card">
<h2>🧪 Diabetes Prediction</h2>
<p>This AI system analyzes medical parameters to estimate the likelihood of diabetes.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Enter Patient Medical Information")

# ------------------ INPUT LAYOUT ------------------
col1, col2, col3 = st.columns(3)

with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        0,20,
        help="Number of times pregnant"
    )

    glucose = st.number_input(
        "Glucose Level",
        help="Plasma glucose concentration"
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        help="Diastolic blood pressure (mm Hg)"
    )


with col2:

    skin_thickness = st.number_input(
        "Skin Thickness",
        help="Triceps skin fold thickness (mm)"
    )

    insulin = st.number_input(
        "Insulin",
        help="2-Hour serum insulin (mu U/ml)"
    )

    bmi = st.number_input(
        "BMI",
        help="Body Mass Index (weight in kg/(height in m)^2)"
    )


with col3:

    dpf = st.number_input(
        "Diabetes Pedigree Function",
        help="Family history of diabetes score"
    )

    age = st.number_input(
        "Age",
        18,120,
        help="Age of the patient"
    )

st.markdown("---")

# ------------------ PREDICTION ------------------

input_data = np.array([[pregnancies, glucose, blood_pressure,
                        skin_thickness, insulin, bmi,
                        dpf, age]])

if st.button("Predict"):

    prediction = model.predict(input_data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")