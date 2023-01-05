#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:00:03 2023

@author: mackenzieporter
"""
#Exercise 3.16

number = int(input('Enter the number:'))
largest = int(input('Enter the number:'))

if number > largest:
    second_largest = largest
    largest = number 
else:
    second_largest = number 
    
for number in range(2,10):
    number = int(input('Enter the number:'))
    
    if number > largest :
        second_largest = largest 
        largest = number 
        
    elif number > second_largest:
        second_largest = number
    
    
print(f'Largest number is {largest}\nSecond largest number is {second_largest}')


    