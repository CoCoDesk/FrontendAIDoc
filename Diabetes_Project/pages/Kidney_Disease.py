import streamlit as st
import pickle
import numpy as np
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Kidney Disease Prediction", layout="wide")

# ---------------- LOAD MODEL ----------------
# Correct path to cancer.pkl (works on Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "kidney.pkl")

# Load Cancer Model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)



# ------------------- HEADER --------------------
st.markdown("""
    <div style="background-color:#f8f9fa; padding:25px; border-radius:20px; 
                box-shadow:0 4px 12px rgba(0,0,0,0.1);">
        <h1 style="text-align:center; font-size:40px; color:#2b6777;">
            🩺 Kidney Disease Prediction
        </h1>
        <p style="text-align:center; font-size:18px; color:#555;">
            Enter the required health parameters below to check the risk of Chronic Kidney Disease.
        </p>
    </div>
    <br>
""", unsafe_allow_html=True)

# ------------------- INPUT FIELDS --------------------
st.subheader("Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 45)
    bp = st.number_input("Blood Pressure (bp)", 50, 200, 80)
    al = st.number_input("Albumin (al)", 0, 5, 0)
    su = st.number_input("Sugar (su)", 0, 5, 0)
    bgr = st.number_input("Blood Glucose Random (bgr)", 50, 500, 120)
    bu = st.number_input("Blood Urea (bu)", 1, 300, 40)
    sc = st.number_input("Serum Creatinine (sc)", 0.1, 15.0, 1.2)

with col2:
    pot = st.number_input("Potassium (pot)", 1.0, 10.0, 4.5)
    pc = st.number_input("Pus Cell (pc)", 0, 1, 0)
    pcc = st.number_input("Pus Cell Clumps (pcc)", 0, 1, 0)
    ba = st.number_input("Bacteria (ba)", 0, 1, 0)
    b = st.number_input("Blood (b)", 0, 1, 0)
    rbc = st.number_input("Red Blood Cells (rbc)", 0, 1, 0)
    wc = st.number_input("White Blood Cell Count (wc)", 1, 30000, 8000)
    htn = st.number_input("Hypertension (htn)", 0, 1, 0)
    dm = st.number_input("Diabetes Mellitus (dm)", 0, 1, 0)

# exactly **18 features** sent here ↓
input_data = np.array([[age, bp, al, su, bgr, bu, sc,
                        pot, pc, pcc, ba, b, rbc,
                        wc, htn, dm, 0, 0]])

# last two zeros are placeholders for removed missing columns to match model shape

# ------------------- PREDICTION --------------------
if st.button("Predict"):
    try:
        pred = model.predict(input_data)[0]

        if pred == 1:
            st.error("⚠ High Risk of Chronic Kidney Disease")
        else:
            st.success("✔ No CKD Detected. You are Safe!")

    except Exception as e:
        st.warning(f"Error: {e}")




