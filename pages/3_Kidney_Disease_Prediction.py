import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Kidney Disease Prediction", page_icon="🧬", layout="wide")

# ---------------- CUSTOM CSS ----------------
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

.result-warning{
background:#fff6e6;
padding:20px;
border-radius:12px;
border-left:6px solid #ffa500;
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

# ---------------- LOAD MODEL ----------------
model_path = Path(__file__).resolve().parents[1] / "models" / "kidney_disease_model.pkl"
model = joblib.load(model_path)

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-card">
<h2>🧬 Kidney Disease Prediction</h2>
<p>This AI system analyzes kidney related clinical parameters to estimate kidney disease risk.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Enter Patient Clinical Information")

# ---------------- INPUT FIELDS ----------------

col1, col2, col3 = st.columns(3)

with col1:

    glucose = st.number_input(
        "Random Blood Glucose (mg/dl)",
        help="Measures blood sugar levels. High levels may indicate diabetes."
    )

    urea = st.number_input(
        "Blood Urea (mg/dl)",
        help="Waste product filtered by kidneys. High levels indicate kidney dysfunction."
    )

    creatinine = st.number_input(
        "Serum Creatinine (mg/dl)",
        help="Important indicator of kidney function."
    )

    sodium = st.number_input(
        "Sodium Level (mEq/L)",
        help="Electrolyte balance indicator."
    )

    potassium = st.number_input(
        "Potassium Level (mEq/L)",
        help="Electrolyte important for heart and kidney function."
    )

with col2:

    wbc = st.number_input(
        "White Blood Cell Count",
        help="High WBC may indicate infection or inflammation."
    )

    egfr = st.number_input(
        "Estimated GFR",
        help="Measures how well kidneys filter blood."
    )

    protein_ratio = st.number_input(
        "Urine Protein-Creatinine Ratio",
        help="Detects protein leakage in urine."
    )

    urine_output = st.number_input(
        "Urine Output (ml/day)",
        help="Reduced urine output may indicate kidney problems."
    )

    pth = st.number_input(
        "Parathyroid Hormone (PTH)",
        help="Hormone affecting calcium balance."
    )

with col3:

    calcium = st.number_input(
        "Serum Calcium",
        help="Calcium imbalance may occur in kidney disease."
    )

    phosphate = st.number_input(
        "Serum Phosphate",
        help="High phosphate may indicate kidney issues."
    )

    bmi = st.number_input(
        "Body Mass Index (BMI)",
        help="BMI indicates body fat level."
    )

    crp = st.number_input(
        "C-Reactive Protein (CRP)",
        help="Marker of inflammation."
    )

    il6 = st.number_input(
        "Interleukin-6 (IL-6)",
        help="Inflammatory cytokine."
    )

st.markdown("---")


# ---------------- PREDICTION ----------------

input_data = np.array([[glucose, urea, creatinine, sodium, potassium,
                        wbc, egfr, protein_ratio, urine_output,
                        pth, calcium, phosphate, bmi, crp, il6]])

if st.button("Predict"):

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("No Kidney Disease")

    elif prediction[0] == 1:
        st.warning("Low Risk Kidney Disease")

    elif prediction[0] == 2:
        st.warning("Moderate Risk Kidney Disease")

    elif prediction[0] == 3:
        st.error("High Risk Kidney Disease")

    else:
        st.error("Severe Kidney Disease")