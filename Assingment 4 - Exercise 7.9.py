#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:31:42 2023

@author: mackenzieporter
"""

# Exercise 7.9 

import numpy as np 

numbers = np.arange(1,16).reshape(3,5)

numbers

# Select row 2

numbers[2]

# Select column 4

numbers[:,4]

# Select rows 0 and 1

numbers[0:2]

# Select columns 2-4

numbers[:,2:5]

# Select the element that is in row 1 and column 4

numbers[1,4]

# Select all elements from rows 1 and 2 that are in columns 0, 2, 4

numbers[1:3, [0, 2, 4]]
