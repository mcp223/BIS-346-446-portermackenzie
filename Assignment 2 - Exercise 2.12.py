#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:31:37 2023

@author: mackenzieporter
"""

#Exercise 2.12

p = 1000
r = 7
print('If you invest $7,000 and receive a 7% annual return, \
      you will receive the following amounts over time ')

#for loop statement to find the range 
for n in range (10,31,10):
    a = p*(1 + r/100)**n
    print('Amount after {} years: ${:.2f}'.format(n,a))

