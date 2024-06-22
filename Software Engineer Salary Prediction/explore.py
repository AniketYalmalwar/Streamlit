import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_exp(x):
    if x == "More than 50 years":
        return 50
    if x == "Less than 1 year":
        return 0.5
    return float(x)

def clean_edu(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Professional degree'
    return "Less than a Bachelors"

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]
    
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_exp)
    df["EdLevel"] = df["EdLevel"].apply(clean_edu)
    
    return df

df = load_data()

def show_explore():
    st.title("Explore Software Engineer Salaries")
    
    st.write("""
             ### Stack Overflow Developer Survey 2023
             """)
    
    st.write("#### Number of Data Points from Different Countries")
    data = df["Country"].value_counts().reset_index()
    data.columns = ["Country", "Count"]
    fig = px.bar(data, x='Country', y='Count', title='Number of Data Points from Different Countries')
    fig.update_layout(height=800)  
    st.plotly_chart(fig)
    
    st.write("#### Average Salary by Country")
    country_salary = df.groupby("Country")["Salary"].mean().reset_index()
    fig = px.choropleth(country_salary, locations="Country", locationmode="country names",
                        color="Salary", hover_name="Country", 
                        color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig)
    
    st.write("#### Mean Salary by Country")
    fig = px.bar(country_salary, x='Country', y='Salary', title='Mean Salary by Country')
    fig.update_layout(height=800) 
    st.plotly_chart(fig)
    
    st.write("#### Experience vs. Salary")
    exp_salary = df.groupby("YearsCodePro")["Salary"].mean().reset_index()
    exp_salary["Experience"] =exp_salary["YearsCodePro"]
    fig = px.line(exp_salary, x="Experience", y='Salary', markers=True, title='Experience vs. Salary')
    st.plotly_chart(fig)

