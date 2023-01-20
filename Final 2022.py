#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:27:01 2023

@author: mackenzieporter
"""

# Final 2022

import pandas as pd
import numpy as np
import pickle

import matplotlib as mpl 
import matplotlib.pyplot as plt

import os

# Changing working directory 

os.getcwd()
os.chdir('/Users/mackenzieporter/Desktop/BUAN 446/Git Repos/BIS-346-446-portermackenzie')

os.getcwd()

# Using Bananas data

# To disable "SettingWithCopyWarning..."
pd.options.mode.chained_assignment = None  

# Reading the data
file = open('Bananas.csv', 'rb')

Bananas = pickle.load(file)

# close the file
file.close()

# Verifying that pickle kept the data types unchanged
Bananas

Bananas.dtypes

# Scatterplot 
plt.style.use('classic')

plt.scatter(Bananas['Bananas_price_per_lb'],Bananas['DATE'],color='red',
            marker='^')
plt.ylabel('Price Per Pound')
plt.xlabel('Date')
plt.title('Banana Prices in the U.S.')
plt.show()

# I was unsure what the graph was looking like due to the inability to load the file into 'Bananas'
# I didn't want to add additional details without knowing what to adjust size wise 

