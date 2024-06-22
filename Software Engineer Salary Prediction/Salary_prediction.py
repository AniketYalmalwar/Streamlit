import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data['le_country']
le_edu = data["le_edu"]

def show_predict():
    st.title("Software Devloper Salary Prediction")
    st.write(""" ### We need some information to predict the salary""")
    
    countries = {'India','United States of America',
       'United Kingdom of Great Britain and Northern Ireland',
       'Australia', 'Netherlands', 'Germany', 'Sweden', 'France', 'Spain',
       'Brazil', 'Italy', 'Canada', 'Switzerland',  'Norway',
       'Denmark', 'Israel', 'Poland'
    }
    
    educations = {'Less than a Bachelors','Bachelor’s degree','Master’s degree','Professional degree'}
    
    country = st.selectbox("Country",countries)
    education = st.selectbox("Education Level",educations)
    
    experience = st.slider("Years of Experience",0,50,3)
    
    ok = st.button("Predict Salary")
    if ok:
        x = np.array([[country,education,experience]])
        x[:,0] = le_country.transform(x[:,0])
        x[:,1] = le_edu.transform(x[:,1])
        x = x.astype(float)
        
        Salary = regressor.predict(x)
        st.subheader(f"The estimated Salary is $ {Salary[0]:.2f}")
        
        
        

    