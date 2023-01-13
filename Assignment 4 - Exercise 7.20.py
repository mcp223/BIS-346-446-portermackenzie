#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:07:09 2023

@author: mackenzieporter
"""

# Exercise 7.20 

import random 

# List elements 

%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 1)]

%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 10)]

%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 100)]
    
%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 1000)]

%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 10000)]
    
%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 100000)]

%timeit elements_list = \
    [random.randrange(1,7) for i in range(0, 1000000)]
    
# Array elements

import numpy as np 

%timeit elements_array = np.random.randint.(1, 7, 1)    

%timeit elements_array = np.random.randint.(1, 7, 10)  

%timeit elements_array = np.random.randint.(1, 7, 100) 

%timeit elements_array = np.random.randint.(1, 7, 1000) 

%timeit elements_array = np.random.randint.(1, 7, 10000)        

%timeit elements_array = np.random.randint.(1, 7, 100000)

%timeit elements_array = np.random.randint.(1, 7, 1000000)   


    
    