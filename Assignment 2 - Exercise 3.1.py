#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:52:23 2023

@author: mackenzieporter
"""

#Exercise 3.1 
#Modify fig03_03 for inputs other than 1 or 2, and calculate failures after

passes = 0 

# Not sure why you're trying to oterate over student, but your script always produces 10 failures   -5
for student in range(10):
    result = int(input('Enter result (1 = pass, 2 = fail):'))

#while stmt for any input other than 1 or 2     

    while result != 1 and result != 2:
        print('Incorrect result entered')
        result = int(input('Enter result (1 = pass, 2 = fail):'))
        
    if result == int(1):
        passes == passes + 1
        
    
print('Passed:', passes)

#caLlculating number of failures after the inputs are received
print('Failed:', 10 - passes)
if passes > 8 :
    print('Bonus to instructor')
    
    