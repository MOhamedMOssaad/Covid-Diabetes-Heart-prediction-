# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:32:04 2022

@author: mosaa
"""
import numpy as np 
import pickle 

load_model = pickle.load(open("F:\Covid 19 _ prediction\covid_model.pkl", 'rb'))

inp_data = (27657145,0.058359,20200123)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(inp_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a covid-19')
else:
  print('The Person has covid-19')