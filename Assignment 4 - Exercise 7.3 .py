#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:14:08 2023

@author: mackenzieporter
"""

# Exercise 7.3 

import numpy as np

numbers = np.arange(2,20,2).reshape(3,3)

numbers 

numbers2 = np.arange(9,0,-1).reshape(3,3)

numbers2

numbers3 = numbers * numbers2 

numbers3

