import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open("diabetes.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Prediction Web App")

st.write("Enter the required details below to check the chances of diabetes:")

# Taking inputs from user
preg = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=5.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Predict button
if st.button("Predict"):
    # Arrange data in correct order
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    # Prediction (0 = No Diabetes, 1 = Has Diabetes)
    result = model.predict(input_data)[0]

    if result == 1:
        st.error("🔴 **High Chance of Diabetes**")

        st.subheader("Recommended Medication / Advice:")
        st.write("""
        - Exercise at least 30 minutes daily  
        - Reduce sugar and processed foods  
        - Prefer whole grains and fiber-rich diet  
        - Take Metformin (only if doctor prescribes)  
        - Regular blood glucose monitoring  
        """)
    else:
        st.success("🟢 **No Diabetes Detected**")

        st.subheader("Healthy Lifestyle Advice:")
        st.write("""
        - Maintain a balanced diet  
        - Keep BMI under control  
        - Regular exercise  
        - Avoid excessive sugary drinks  
        """)

