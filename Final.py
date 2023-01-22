# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:59:50 2023

@author: troya
"""
# Final 2022



import pandas as pd

import numpy as np

import pickle



import matplotlib as mpl 

import matplotlib.pyplot as plt



import os



# Changing working directory 


# You are hard-wiring the directory. No such exists on my computer   -10
os.getcwd()

os.chdir('/Users/mackenzieporter/Desktop/BUAN 446/Git Repos/BIS-346-446-portermackenzie')



os.getcwd()



# Using Bananas data



# To disable "SettingWithCopyWarning..."

pd.options.mode.chained_assignment = None  



# Reading the data

file = open('Bananas.csv', 'rb')



Bananas = pickle.load(file)
# Pickel does not work with csv files. You need to use pd.read_csv   -10


# close the file

file.close()



# Verifying that pickle kept the data types unchanged

Bananas = bananas



Bananas.dtypes



# Scatterplot 

plt.style.use('classic')



plt.scatter(Bananas['Bananas_price_per_lb'],Bananas['DATE'],color='red',

            marker='^')

# You failed to convert DATE from strings  -10

plt.ylabel('Price Per Pound')

plt.xlabel('Date')

plt.title('Banana Prices in the U.S.')

plt.show()