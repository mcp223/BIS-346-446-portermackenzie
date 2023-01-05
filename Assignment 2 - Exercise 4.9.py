#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:00:42 2023

@author: mackenzieporter
"""
#Exercise 4.9

def Fahrenheit(C):
    F = (9 / 5) * C + 32
    return F

#printing results into a table
print('Celcius Fahrenheit')
for x in range(0,101):
    print(x,'\t','\t', round(Fahrenheit(x),1))