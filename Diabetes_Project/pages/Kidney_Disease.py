import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Kidney Disease Predictor", layout="wide")

# ---------------- STYLING ----------------
st.markdown("""
    <style>
        body {
            background-color: white;
        }
        .title {
            font-size: 40px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #4F4F4F;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🩺 Kidney Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter patient details below to check kidney health</div>', unsafe_allow_html=True)

# ---------------- INPUT FORM ----------------
with st.form("kidney_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        bp = st.number_input("Blood Pressure (mm/Hg)", min_value=50, max_value=200)
        sg = st.number_input("Specific Gravity", min_value=1.000, max_value=1.050, step=0.001, format="%.3f")
        al = st.number_input("Albumin Level", min_value=0, max_value=5, step=1)
        su = st.number_input("Sugar Level", min_value=0, max_value=5, step=1)

    with col2:
        rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
        pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
        pcc = st.selectbox("Pus Cell Clumps", ["present", "not present"])
        ba = st.selectbox("Bacteria", ["present", "not present"])
        bgr = st.number_input("Blood Glucose Random", min_value=50, max_value=500)
        bu = st.number_input("Blood Urea", min_value=1, max_value=300)

    submitted = st.form_submit_button("Predict")

# ---------------- RESULT SECTION ----------------
if submitted:
    st.warning("⚠️ Prediction model not connected yet.")
    st.info("🔧 Please integrate the ML model once ready.")

