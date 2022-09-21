# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:30:51 2022

@author: mosaa
"""

import numpy as np 
import pickle 
import streamlit as st

load_model = pickle.load(open("F:\Covid 19 _ prediction\covid_model.pkl", 'rb'))

def covid_prediction (inp_data):
    
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(inp_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        return 'The Person does not have a covid-19'
    else:
        return 'The Person has covid-19'
        
        
def main():
    #title of the page 
    st.title('Covid-19 prediction web App') 
    
    #get inputs
    
    Population = st.text_input('number of Population')
    Date = st.text_input('Enter your Date')
    Weight = st.text_input('Enter your Weight')
    #our code 
    cov = ''
    
    if st.button('covid-19 test the result of the person'):
        cov = covid_prediction([Population,Date,Weight])
        
    st.success(cov)

if __name__ == '__main__':
    main()
        
