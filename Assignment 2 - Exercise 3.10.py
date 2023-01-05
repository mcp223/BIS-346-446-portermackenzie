#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:53:45 2023

@author: mackenzieporter
"""

#Exercise 3.10

p = 7000 
r = 7
print('If you invest $7,000 and receive a 7% annual return, \
      you will receive the following amounts over the next 30 years ')
     
for n in range(10,31):
    a = p*(1 + r/100)**n
    print('Amount after {} years: ${:.2f}.'.format(n,a))        