# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:30:51 2022

@author: mosaa
"""

import numpy as np 
import pickle 
import streamlit as st

load_model = pickle.load(open("F:\Diabetes_prediction_model\diabetes_model.sav", 'rb'))

def diabetes_prediction (input_data):
    
   # change the input data to a numpy array
   input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

   prediction = load_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0]== 0):
         return 'The Person does not have a diabetes'
   else:
         return 'The Person has diabetes'
        
        
def main():
    #title of the page 
    st.title('diabetes prediction web App') 
    #HighBP	HighChol	CholCheck	BMI	Smoker	Stroke	HeartDiseaseorAttack	PhysActivity	Veggies	HvyAlcoholConsump	GenHlth	MentHlth	PhysHlth	DiffWalk	Age	Education	Income
    #get inputs
    
    HighBP = st.text_input('percentage of HighBP')
    HighChol = st.text_input('percentage of HighChol')
    CholCheck = st.text_input('percentage of CholCheck')
    BMI = st.text_input('numcer of BMI')
    Smoker = st.text_input('Smoker or Not Smoker')
    Stroke = st.text_input('Stroke  or Not has Stroke')
    HeartDiseaseorAttack = st.text_input('HeartDiseaseorAttack  or Not has HeartDiseaseorAttack')
    PhysActivity = st.text_input('PhysActivity  or Not doing a PhysActivity')
    Veggies = st.text_input('Eating Veggies  or Not')
    HvyAlcoholConsump = st.text_input('Has a HvyAlcoholConsump or Not ')
    GenHlth = st.text_input('percentage of GenHlth')
    MentHlth = st.text_input('percentage of MentHlth')
    PhysHlth = st.text_input('percentage of PhysHlth')
    DiffWalk = st.text_input('percentage of DiffWalk')
    Age = st.text_input('what is your age')
    Education = st.text_input('educationed or not')
    Income = st.text_input('percentage of Income')

    #our code 
    dia = ''
    
    if st.button('Diabetes test the result of the person'):
        dia = diabetes_prediction([HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,Veggies,HvyAlcoholConsump,GenHlth,MentHlth,PhysHlth,DiffWalk,Age,Education,Income])
        
    st.success(dia)

if __name__ == '__main__':
    main()
        
