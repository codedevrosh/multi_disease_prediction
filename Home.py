import streamlit as st

st.set_page_config(
    page_title="Multi Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>


.card{
background:#111827;
padding:35px;
border-radius:18px;
text-align:center;
border:1px solid #1f2937;
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
transition:0.3s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0px 12px 30px rgba(0,0,0,0.35);
}

.card-icon{
font-size:45px;
margin-bottom:10px;
}

.card-title{
font-size:26px;
font-weight:700;
margin-bottom:8px;
}

.card-text{
color:#9ca3af;
font-size:15px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
"""
<h1 style='text-align: center; font-size:65px; color:#4da6ff;'>
Multi Disease Prediction System
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style='text-align:center; font-size:24px; color:#cbd5e1;'>
AI-powered system to predict diseases using Machine Learning
</p>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ---------- CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🫀</div>
        <div class="card-title">Heart Disease</div>
        <div class="card-text">
        Predict heart disease risk using clinical patient data.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🧪</div>
        <div class="card-title">Diabetes</div>
        <div class="card-text">
        Analyze glucose levels and health indicators.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🧬</div>
        <div class="card-title">Kidney Disease</div>
        <div class="card-text">
        Detect kidney disease using medical parameters.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.info("⬅ Select a disease from the sidebar to start prediction")