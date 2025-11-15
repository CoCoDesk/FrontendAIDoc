import streamlit as st
import pickle
import numpy as np

# Load trained heart disease model
with open("heart.pkl", "rb") as file:
    model = pickle.load(file)

st.title("❤️ Heart Disease Prediction Web App")
st.write("Enter the required details below to check your heart health:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=250, value=120)
chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
restecg = st.selectbox("Rest ECG (0–2)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise-Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of ST Segment (0–2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])

# Predict button
if st.button("Predict"):

    # Format input for prediction EXACTLY as model was trained
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

    try:
        result = model.predict(input_data)[0]

        if result == 1:
            st.error("🔴 **High Chance of Heart Disease**")

            st.subheader("Recommended Medication / Advice:")
            st.write("""
            **🔹 Lifestyle & Diet**
            - Reduce salt and saturated fat  
            - Daily walking for 30–45 minutes  
            - Maintain healthy weight  
            - Quit smoking/alcohol  

            **🔹 Medicines (Only After Doctor Consultation)**
            - Statins (to lower cholesterol)  
            - Aspirin (blood thinner)  
            - Beta-blockers  
            - ACE inhibitors  

            **🔹 Monitoring**
            - Regular BP checkups  
            - Annual ECG & Stress Test  
            """)

        else:
            st.success("🟢 **No Heart Disease Detected**")

            st.subheader("Healthy Heart Tips:")
            st.write("""
            - Maintain a balanced diet  
            - Exercise regularly  
            - Avoid stress  
            - Keep your cholesterol in control  
            - Get regular health checkups  
            """)

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.info("Make sure your model is trained on exactly 13 features.")
