#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:46:36 2023

@author: mackenzieporter
"""

# Exercise 5.28

import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

import statistics as stats


responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

values, counts = np.unique(responses, return_counts = True)
values = list(values)
counts = list(counts)

print('Responses and Frequencies')
for value, count in zip(values, counts):
    print(f'{value}: {count}')
    

print('Minimum:', min(responses))
print('Maximum:', max(responses))
print('Range:', max(responses) - min(responses))
print('Median:', stats.median(responses))
print('Mean:', stats.mean(responses))
print('Mode:', stats.mode(responses))
print('Variance:', stats.variance(responses))
print('Standard Deviation:', stats.stdev(responses))
