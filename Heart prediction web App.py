# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:30:51 2022

@author: mosaa
"""

import numpy as np 
import pickle 
import streamlit as st

load_model = pickle.load(open("F:\heart_model_prediction\model_diabetes_prediction.sav", 'rb'))

def heart_prediction (input_data):
    
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
            return  'The Person does not have a Heart Disease'
    else:
            return  'The Person has Heart Disease' 
        
        
def main():
    #title of the page 
    st.title('Heart prediction web App') 
    
    #get inputs
    
    HighBP = st.text_input('percentage of HighBP')
    HighChol = st.text_input('percentage of HighChol')
    CholCheck = st.text_input('percentage of CholCheck')
    BMI = st.text_input('numcer of BMI')
    Smoker = st.text_input('Smoker or Not Smoker')
    Stroke = st.text_input('Stroke  or Not has Stroke')
    Diabetes = st.text_input('Diabetes  or Not has Diabetes')
    PhysActivity = st.text_input('PhysActivity  or Not doing a PhysActivity')
    Fruits = st.text_input('Eating Fruits  or Not ')
    Veggies = st.text_input('Eating Veggies  or Not')
    GenHlth = st.text_input('percentage of GenHlth')
    MentHlth = st.text_input('percentage of MentHlth')
    PhysHlth = st.text_input('percentage of PhysHlth')
    DiffWalk = st.text_input('percentage of DiffWalk')
    Sex = st.text_input('male or female')
    Age = st.text_input('what is your age')
    Education = st.text_input('educationed or not')
    Income = st.text_input('percentage of Income')

    #our code 
    dis = ''
    
    if st.button('Heart disease test the result of the person'):
        dis = heart_prediction([HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,Diabetes,PhysActivity,Fruits,Veggies,GenHlth,MentHlth,PhysHlth,DiffWalk,Sex,Age,Education,Income])
        
    st.success(dis)

if __name__ == '__main__':
    main()
        
