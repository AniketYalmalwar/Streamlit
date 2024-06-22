import streamlit as st
from Salary_prediction import show_predict
from explore import show_explore


page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))
if page =="Predict":
    show_predict()
else:
    show_explore()