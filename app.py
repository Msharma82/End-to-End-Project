"""
Information : 
Age [integer] , 
BP {Low:1, Normal:2, High:3},
Cholesterol {Normal:1, High:2}
Sodium_to_Potasium [Float]
Gender [F,M] [on hot encoded] [Gender_female,Gender_male]  
"""

import streamlit  as st
import pandas as pd
import numpy as np
import pickle


with open("decision_tree.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Decision Tree Classifier App")
st.subheader("Apollo project")

age = st.slider("Age",1,100,1)
Gender =  st.radio("Gender", ["Female","Male"])
Bp = st.selectbox("Blood Pressure", ["Low","Normal","High"]) # Normal
Cholestrol = st.selectbox("Cholestrol", ["Normal","High"])
Sodium_to_Potasium = st.number_input("Sodium_to_Potasium", 
                                     min_value=0.0, 
                                     max_value=30.0,
                                     value=1.0)
bp_mapping = {"Low":1, "Normal":2, "High":3}
Bp = bp_mapping[Bp]
Cholestrol_mapping = {"Normal":1, "High":2}
Cholestrol = Cholestrol_mapping[Cholestrol]
if Gender == "Female":
    gender_female = 1
    gender_male = 0
else:
    gender_female = 0
    gender_male = 1

input_array = np.array([[age,Bp,Cholestrol,Sodium_to_Potasium,gender_female,gender_male]])
if st.button("Submit"):
    st.write(f"input array is {input_array}")
    drug = model.predict(input_array)
    st.write(f"Drug prescribed as {drug}")



#Age,bp,chel,na_to_k,gender

