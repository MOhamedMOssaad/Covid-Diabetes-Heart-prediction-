# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:31:32 2022

@author: mosaa
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("F:/multiple diseases detection/Diabetes_prediction_model/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("F:/multiple diseases detection/heart_model_prediction/model_diabetes_prediction.sav",'rb'))

covid_19_model = pickle.load(open("F:/multiple diseases detection/Covid 19 _ prediction/covid_model.pkl", 'rb'))


with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'covid-19 Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        HighBP = st.text_input('Number of HighBP')
        
    with col2:
        HighChol = st.text_input('Number of HighChol ')
    
    with col3:
        CholCheck = st.text_input('CholCheck value')
    
    with col1:
        BMI = st.text_input('BMI value')
    
    with col2:
        Smoker = st.text_input('Smoker or not')
    
    with col3:
        Stroke = st.text_input('Have a Stroke or not')
    
    with col1:
        HeartDiseaseorAttack = st.text_input('HeartDiseaseorAttack value')
    
    with col2:
        PhysActivity = st.text_input('PhysActivity value')
     
    with col3:
        Veggies = st.text_input('Have a Veggies or not')
        
    with col1:
        HvyAlcoholConsump = st.text_input('HvyAlcoholConsump value')
    
    with col2:
        GenHlth = st.text_input('GenHlth value')
     
    with col3:
        MentHlth = st.text_input('MentHlth value')
       
    with col1:
        PhysHlth = st.text_input('PhysHlth value')
    
    with col2:
        DiffWalk = st.text_input('DiffWalk value')
     
    with col3:
        Age = st.text_input('Age of the person')
        
    with col1:
        Education = st.text_input('Education value')
    
    with col2:
        Income = st.text_input('Income value')
        
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,Veggies,HvyAlcoholConsump,GenHlth,MentHlth,PhysHlth,DiffWalk,Age,Education,Income]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
   # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        HighBP = st.text_input('Number of HighBP')
        
    with col2:
        HighChol = st.text_input('Number of HighChol ')
    
    with col3:
        CholCheck = st.text_input('CholCheck value')
    
    with col1:
        BMI = st.text_input('BMI value')
    
    with col2:
        Smoker = st.text_input('Smoker or not')
    
    with col3:
        Stroke = st.text_input('Have a Stroke or not')
    
    with col1:
       Diabetes  = st.text_input('Diabetes value')
    
    with col2:
        PhysActivity = st.text_input('PhysActivity value')
     
    with col3:
        Fruits = st.text_input('Fruits value')
        
    with col1:
        Veggies = st.text_input('Have a Veggies or not')
         
    with col2:
        GenHlth = st.text_input('GenHlth value')
     
    with col3:
        MentHlth = st.text_input('MentHlth value')
       
    with col1:
        PhysHlth = st.text_input('PhysHlth value')
    
    with col2:
        DiffWalk = st.text_input('DiffWalk value')
        
    with col3:
        Sex = st.text_input('Sex value')
     
    with col1:
        Age = st.text_input('Age of the person')
        
    with col2:
        Education = st.text_input('Education value')
    
    with col3:
        Income = st.text_input('Income value')
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,Diabetes,PhysActivity,Fruits,Veggies,GenHlth,MentHlth,PhysHlth,DiffWalk,Sex,Age,Education,Income]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "covid-19 Prediction"):
    
    # page title
    st.title("covid-19 Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        Population = st.text_input('Population value')
        
    with col2:
        Weight = st.text_input('Weight value')    
        
    with col3:
        Date = st.text_input('Date value')
        
  
        
    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("covid-19's Test Result"):
        covid_prediction = covid_19_model.predict([[Population,Weight,Date]])                          
        covid_diagnosis = covid_prediction
    st.success(covid_diagnosis)
    