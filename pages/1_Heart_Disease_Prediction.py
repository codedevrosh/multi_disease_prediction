import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Heart Disease Prediction", page_icon="🫀", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

.main-card{
background: linear-gradient(135deg,#ff5f6d,#ff2e63);
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
model_path = Path(__file__).resolve().parents[1] / "models" / "heart_disease_model.pkl"
model = joblib.load(model_path)

# ------------------ HEADER ------------------
st.markdown("""
<div class="main-card">
<h2>🫀 Heart Disease Prediction</h2>
<p>This AI system analyzes clinical parameters to estimate the likelihood of heart disease.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Enter Patient Medical Information")

# ------------------ INPUT LAYOUT ------------------
col1, col2, col3 = st.columns(3)

with col1:

    age = st.number_input(
        "Age",
        18,120,
        help="Age of the patient in years"
    )

    sex = st.selectbox(
        "Sex",
        ["Male","Female"],
        help="Biological sex of the patient"
    )

    cp = st.selectbox(
        "Chest Pain Type",
        ["Typical Angina","Atypical Angina","Non-anginal Pain","Asymptomatic"],
        help="Type of chest pain experienced by the patient"
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        help="Blood pressure measured while patient is at rest (mm Hg)"
    )
    thal = st.selectbox(
        "Thalassemia",
        ["Normal", "Fixed Defect", "Reversible Defect"],
        help="Blood disorder affecting oxygen transport"
    )


with col2:

    chol = st.number_input(
        "Cholesterol",
        help="Serum cholesterol level in mg/dl"
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar",
        ["Normal (≤120 mg/dl)","High (>120 mg/dl)"],
        help="Fasting blood glucose level"
    )

    restecg = st.selectbox(
        "Resting ECG",
        ["Normal","ST-T Wave Abnormality","Left Ventricular Hypertrophy"],
        help="Electrocardiogram result"
    )

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        help="Maximum heart rate achieved during exercise test"
    )


with col3:

    exang = st.selectbox(
        "Exercise Induced Angina",
        ["No","Yes"],
        help="Chest pain triggered by exercise"
    )

    oldpeak = st.number_input(
        "Oldpeak",
        help="ST depression induced by exercise relative to rest"
    )

    slope = st.selectbox(
        "Slope",
        ["Upsloping","Flat","Downsloping"],
        help="Slope of peak exercise ST segment"
    )

    ca = st.selectbox(
        "Major Vessels",
        [0,1,2,3],
        help="Number of major vessels colored by fluoroscopy"
    )



st.markdown("---")

# ------------------ CONVERT INPUTS ------------------

sex = 1 if sex=="Male" else 0

cp_dict = {
"Typical Angina":0,
"Atypical Angina":1,
"Non-anginal Pain":2,
"Asymptomatic":3
}
cp = cp_dict[cp]

fbs = 1 if fbs=="High (>120 mg/dl)" else 0

restecg_dict={
"Normal":0,
"ST-T Wave Abnormality":1,
"Left Ventricular Hypertrophy":2
}
restecg = restecg_dict[restecg]

exang = 1 if exang=="Yes" else 0

slope_dict={
"Upsloping":0,
"Flat":1,
"Downsloping":2
}
slope = slope_dict[slope]

thal_dict={
"Normal":1,
"Fixed Defect":2,
"Reversible Defect":3
}
thal = thal_dict[thal]

# ------------------ PREDICTION ------------------

input_data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,
                        thalach,exang,oldpeak,slope,ca,thal]])

if st.button("Predict"):

    prediction = model.predict(input_data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")
