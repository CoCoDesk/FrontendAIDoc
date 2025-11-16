# import streamlit as st
# import pickle
# import numpy as np
# import os

# # Correct path to liver.pkl (works on Streamlit Cloud)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_PATH = os.path.join(BASE_DIR, "liver.pkl")

# # Load trained liver disease model
# with open(MODEL_PATH, "rb") as file:
#     model = pickle.load(file)

# st.title("🧬 Liver Disease Prediction Web App")
# st.write("Enter the required details below to check liver health:")

# # User Inputs
# age = st.number_input("Age", min_value=1, max_value=120, value=45)
# gender = st.selectbox("Gender (1 = Male, 0 = Female)", [1, 0])
# total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=75.0, value=1.0)
# direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=30.0, value=0.5)
# alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=50, max_value=3000, value=250)
# alamine_aminotransferase = st.number_input("Alamine Aminotransferase (ALT)", min_value=5, max_value=3000, value=30)
# aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase (AST)", min_value=5, max_value=3000, value=40)
# total_proteins = st.number_input("Total Proteins", min_value=0.0, max_value=10.0, value=6.5)
# albumin = st.number_input("Albumin", min_value=0.0, max_value=10.0, value=3.0)
# ag_ratio = st.number_input("A/G Ratio", min_value=0.0, max_value=3.0, value=1.0)

# # Predict button
# if st.button("Predict"):

#     # Format input for prediction exactly as model was trained
#     input_data = np.array([[age, gender, total_bilirubin, direct_bilirubin,
#                             alkaline_phosphotase, alamine_aminotransferase,
#                             aspartate_aminotransferase, total_proteins,
#                             albumin, ag_ratio]])

#     try:
#         result = model.predict(input_data)[0]

#         if result == 1:
#             st.error("🔴 **High Chance of Liver Disease**")

#             st.subheader("Medical Advice:")
#             st.write("""
#             **🔹 Lifestyle & Diet**
#             - Avoid alcohol completely  
#             - Reduce oily and fatty foods  
#             - Drink 3–4 liters of water daily  
#             - Eat high-fiber foods (vegetables, fruits)  

#             **🔹 Medicines (Only Under Doctor's Guidance)**
#             - Silymarin  
#             - Ursodeoxycholic acid (UDCA)  
#             - Vitamin supplements  

#             **🔹 Important Tests**
#             - Liver Function Test (LFT)  
#             - Ultrasound Abdomen  
#             - Gamma-GT  
#             """)

#         else:
#             st.success("🟢 **No Liver Disease Detected**")

#             st.subheader("Healthy Liver Tips:")
#             st.write("""
#             - Stay hydrated  
#             - Avoid heavy alcohol  
#             - Maintain healthy weight  
#             - Exercise regularly  
#             - Reduce junk foods  
#             """)

#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#         st.info("Make sure your liver model is trained on exactly 10 features.")





import streamlit as st
import pickle
import numpy as np
import os

# Correct path to liver.pkl
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "liver.pkl")

# Load model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

st.title("🧬 Liver Disease Prediction Web App")
st.write("Enter the patient details below:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=45)

# Your model expects encoded values → 1 for Male, 0 for Female
gender_str = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender_str == "Male" else 0   # 🔥 FIXED

total_bil = st.number_input("Total Bilirubin", min_value=0.0, max_value=75.0, value=1.0)
direct_bil = st.number_input("Direct Bilirubin", min_value=0.0, max_value=30.0, value=0.5)
alkphos = st.number_input("Alkaline Phosphotase", min_value=50, max_value=3000, value=250)
alt = st.number_input("Alamine Aminotransferase (ALT)", min_value=5, max_value=3000, value=30)
ast = st.number_input("Aspartate Aminotransferase (AST)", min_value=5, max_value=3000, value=40)
proteins = st.number_input("Total Proteins", min_value=0.0, max_value=10.0, value=6.5)
albumin = st.number_input("Albumin", min_value=0.0, max_value=10.0, value=3.0)
ag_ratio = st.number_input("A/G Ratio", min_value=0.0, max_value=3.0, value=1.0)

if st.button("Predict"):

    # Make sure features match EXACT model training order
    input_data = np.array([[age, gender, total_bil, direct_bil,
                            alkphos, alt, ast, proteins,
                            albumin, ag_ratio]])

    result = model.predict(input_data)[0]  # Result is 1 or 2

    # ILPD label meaning:
    # 1 = Liver Disease
    # 2 = No Liver Disease

    if result == 1:
        st.error("🔴 **High Chance of Liver Disease**")
        st.subheader("Advice:")
        st.write("""
        - Avoid alcohol  
        - Reduce fatty foods  
        - Drink plenty of fluids  
        - Consult a hepatologist  
        - Take LFT & ultrasound  
        """)
    else:
        st.success("🟢 **No Liver Disease Detected**")
        st.subheader("Healthy Liver Tips:")
        st.write("""
        - Stay hydrated  
        - Avoid junk foods  
        - Exercise regularly  
        - Avoid excessive alcohol  
        """)
