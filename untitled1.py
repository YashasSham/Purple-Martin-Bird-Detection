# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:41:30 2018

@author: Yasha
"""

import csv
import matplotlib.pyplot as plt 

with open('validation_output.csv', 'r') as f:
    reader = csv.reader(f)
    validation_list = list(reader)
    
validation_output = [item for sublist in validation_list for item in sublist]

for i in range(len(validation_output)):
    validation_output[i] = float(validation_output[i])


with open('training_output.csv', 'r') as f:
    reader = csv.reader(f)
    training_list = list(reader)
    
training_output = [item for sublist in training_list for item in sublist]

for i in range(len(training_output)):
    training_output[i] = float(training_output[i])

plt.plot(validation_output, label='Validation')
plt.plot(training_output, label='Training')
plt.legend()
plt.show()