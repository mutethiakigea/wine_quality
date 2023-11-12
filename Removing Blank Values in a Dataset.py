#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# File paths
input_file_path = r'C:\Users\Administrator\Downloads\winequality-red.csv'
output_file_path = r'C:\Users\Administrator\Downloads\winequality-red_processed.csv'


# In[3]:


# Load the CSV file using numpy's genfromtxt function
data = np.genfromtxt(input_file_path, delimiter=',', skip_header=1, filling_values=np.nan)


# In[4]:


# Replace all blank values in the quality column with NAN
data[:, -1][np.isnan(data[:, -1])] = np.nan


# In[5]:


# Save the processed data into a new CSV file
np.savetxt(output_file_path, data, delimiter=',', header='fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality', comments='')


# In[6]:


print(f"Processed data saved to: {output_file_path}")

