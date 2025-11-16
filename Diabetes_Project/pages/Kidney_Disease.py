import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
from streamlit_lottie import st_lottie
import json

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Kidney Disease Predictor", layout="wide")

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #ffffff, #e3f2fd, #ffffff);
    background-size: 400% 400%;
    animation: bgAnimation 12s ease infinite;
}
@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
}

.header-box {
    animation: fadeIn 1s ease-in-out;
    text-align: center;
    padding: 25px;
    background: linear-gradient(135deg, #0d47a1, #1976d2);
    color: white;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
}

.card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    transition: 0.3s;
    border: 1px solid #bbdefb;
}
.card:hover {
    transform: scale(1.03);
    border-color: #1e88e5;
}

.predict-btn button {
    background-color: #1e88e5 !important;
    color: white !important;
    padding: 10px 25px;
    font-size: 18px;
    border-radius: 10px;
    transition: 0.3s;
}
.predict-btn button:hover {
    background-color: #0d47a1 !important;
    transform: scale(1.05);
}

.result-box {
    margin-top: 25px;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER + TYPEWRITER
# ---------------------------------------------------------
st.markdown("""
<div class="header-box">
    <h1>🩺 Kidney Disease Prediction</h1>
    <h3 id="typewriter"></h3>
</div>

<script>
let text = "A Smart AI-Powered Medical Screening Tool";
let i = 0;

function typeWriter() {
    if (i < text.length) {
        document.getElementById("typewriter").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 60);
    }
}
typeWriter();
</script>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
model = pickle.load(open("kidney.pkl", "rb"))

# ---------------------------------------------------------
# OPTIONAL LOTTIE
# ---------------------------------------------------------
def load_lottie(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return None

lottie = load_lottie("kidney.json")
if lottie:
    st_lottie(lottie, height=220)

# ---------------------------------------------------------
# INPUT FORM — EXACT 18 FEATURES
# ---------------------------------------------------------
st.markdown("### 🧪 Enter Patient Details")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120)
        bp = st.number_input("Blood Pressure", 50, 180)
        al = st.selectbox("Albumin", [0,1,2,3,4,5])
        su = st.selectbox("Sugar", [0,1,2,3,4,5])
        rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])

    with col2:
        pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
        pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
        ba = st.selectbox("Bacteria", ["present", "notpresent"])
        bgr = st.number_input("Blood Glucose Random", 50, 500)
        bu = st.number_input("Blood Urea", 1, 300)

    with col3:
        sc = st.number_input("Serum Creatinine", 0.1, 20.0)
        pot = st.number_input("Potassium", 1.0, 10.0)
        wc = st.number_input("White Blood Cell Count", 1000, 20000)
        htn = st.selectbox("Hypertension", ["yes", "no"])
        dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
        cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
        pe = st.selectbox("Pedal Edema", ["yes", "no"])
        ane = st.selectbox("Anemia", ["yes", "no"])

# ---------------------------------------------------------
# CATEGORICAL MAPPING
# ---------------------------------------------------------
map_yesno = {"yes": 1, "no": 0}
map_binary = {"normal": 1, "abnormal": 0}
map_pcc = {"present": 1, "notpresent": 0}

rbc = map_binary[rbc]
pc = map_binary[pc]
pcc = map_pcc[pcc]
ba = map_pcc[ba]
htn = map_yesno[htn]
dm = map_yesno[dm]
cad = map_yesno[cad]
pe = map_yesno[pe]
ane = map_yesno[ane]

# ---------------------------------------------------------
# FINAL INPUT ORDER (18 FEATURES)
# ---------------------------------------------------------
input_data = np.array([[
    age, bp, al, su, rbc, pc, pcc, ba, bgr, bu,
    sc, pot, wc, htn, dm, cad, pe, ane
]])

# ---------------------------------------------------------
# PREDICT
# ---------------------------------------------------------
if st.button("🔍 Predict", key="predict_btn"):
    with st.spinner("Analyzing health parameters..."):
        time.sleep(1)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.markdown(
            "<div class='result-box' style='background:#ffebee; color:#b71c1c;'>"
            "<b>⚠️ High Risk of Kidney Disease</b><br>Consult a doctor immediately."
            "</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<div class='result-box' style='background:#e8f5e9; color:#1b5e20;'>"
            "<b>✅ You are Healthy</b><br>No signs of kidney disease detected."
            "</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<hr>
<div style='text-align:center; padding:10px; color:#0d47a1;'>
© 2025 Family AI Doctor — Kidney Disease Module
</div>
""", unsafe_allow_html=True)
