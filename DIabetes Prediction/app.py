import streamlit as st
import numpy as np
import pickle

with open('classifier_scaler.pkl', 'rb') as file:
    classifier, scaler = pickle.load(file)

def predict_diabetes(input_data):
    input_data_np_array = np.asarray(input_data)
    input_data_reshaped = input_data_np_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    return prediction

st.title("Diabetes Prediction App")

st.header("Enter the following details:")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose", min_value=0, max_value=200, value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=0)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=0)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.0)
    age = st.number_input("Age", min_value=0, max_value=120, value=0)

if st.button("Predict"):
    input_data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
    prediction = predict_diabetes(input_data)
    
    if prediction[0] == 0:
        st.success("The person is not diabetic")
    else:
        st.error("The person is diabetic")

