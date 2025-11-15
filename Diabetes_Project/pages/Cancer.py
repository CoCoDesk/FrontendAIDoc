import streamlit as st
import numpy as np
import pickle

# Load Cancer Model
with open("cancer.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🩺 Cancer Prediction Web App")

st.write("Enter the details below:")

# 26 FEATURES
texture_mean = st.number_input("Texture Mean", 0.0, 50.0, 10.0)
perimeter_mean = st.number_input("Perimeter Mean", 0.0, 200.0, 70.0)
smoothness_mean = st.number_input("Smoothness Mean", 0.0, 1.0, 0.1)
compactness_mean = st.number_input("Compactness Mean", 0.0, 1.0, 0.1)
concavity_mean = st.number_input("Concavity Mean", 0.0, 1.0, 0.1)
concave_points_mean = st.number_input("Concave Points Mean", 0.0, 1.0, 0.05)
symmetry_mean = st.number_input("Symmetry Mean", 0.0, 1.0, 0.2)
texture_se = st.number_input("Texture SE", 0.0, 50.0, 1.0)
perimeter_se = st.number_input("Perimeter SE", 0.0, 10.0, 1.0)
smoothness_se = st.number_input("Smoothness SE", 0.0, 1.0, 0.01)
compactness_se = st.number_input("Compactness SE", 0.0, 1.0, 0.1)
concavity_se = st.number_input("Concavity SE", 0.0, 1.0, 0.1)
concave_points_se = st.number_input("Concave Points SE", 0.0, 1.0, 0.05)
symmetry_se = st.number_input("Symmetry SE", 0.0, 1.0, 0.2)
fractal_dimension_se = st.number_input("Fractal Dimension SE", 0.0, 1.0, 0.05)
radius_worst = st.number_input("Radius Worst", 0.0, 50.0, 20.0)
texture_worst = st.number_input("Texture Worst", 0.0, 50.0, 25.0)
perimeter_worst = st.number_input("Perimeter Worst", 0.0, 200.0, 100.0)
area_worst = st.number_input("Area Worst", 0.0, 5000.0, 1000.0)
smoothness_worst = st.number_input("Smoothness Worst", 0.0, 1.0, 0.1)
compactness_worst = st.number_input("Compactness Worst", 0.0, 1.0, 0.1)
concavity_worst = st.number_input("Concavity Worst", 0.0, 1.0, 0.1)
concave_points_worst = st.number_input("Concave Points Worst", 0.0, 1.0, 0.1)
symmetry_worst = st.number_input("Symmetry Worst", 0.0, 1.0, 0.2)
fractal_dimension_worst = st.number_input("Fractal Dimension Worst", 0.0, 1.0, 0.1)
area_mean = st.number_input("Area Mean", 0.0, 3000.0, 600.0)

# Prediction
if st.button("Predict"):

    input_data = np.array([[texture_mean, perimeter_mean, smoothness_mean,
                            compactness_mean, concavity_mean, concave_points_mean,
                            symmetry_mean, texture_se, perimeter_se, smoothness_se,
                            compactness_se, concavity_se, concave_points_se,
                            symmetry_se, fractal_dimension_se, radius_worst,
                            texture_worst, perimeter_worst, area_worst, smoothness_worst,
                            compactness_worst, concavity_worst, concave_points_worst,
                            symmetry_worst, fractal_dimension_worst, area_mean]])

    result = model.predict(input_data)[0]

    if result == 1:
        st.error("🔴 HIGH Chance of Cancer (Malignant)")
    else:
        st.success("🟢 LOW Chance of Cancer (Benign)")
