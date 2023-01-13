#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:23:58 2023

@author: mackenzieporter
"""

# Exercise 7.5
import numpy as np

numbers = np.array([2 ** x for x in range(0,6)]).reshape(2,3)

numbers

numbers.flatten()

numbers

numbers.ravel()

numbers
