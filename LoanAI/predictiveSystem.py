# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:10:32 2022

@author: ARTHUR
"""

import numpy as np
import pickle

#loading the saved model
#rb read binary file
loaded_model=pickle.load(open('./trained_model.sav','rb'))

input_data=(1,1,4,1,0,9504,0.0,275.0,360.0,1.0,0)
#changing the input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
    print('You are denied loan')
else:
    print('You are granted loan')