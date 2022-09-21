# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:32:04 2022

@author: mosaa
"""
import numpy as np 
import pickle 

load_model = pickle.load(open("F:\heart_model_prediction\model_diabetes_prediction.sav", 'rb'))

input_data = (1.0,1.0,1.0,40.0,1.0,0.0,0.0,0.0,0.0,1.0,5.0,18.0,15.0,1.0,0.0,45.0,4.0,3.0)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')