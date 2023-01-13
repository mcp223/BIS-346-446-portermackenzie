#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:31:13 2023

@author: mackenzieporter
"""

# Exercise 5.20 

numbers = [[2, 4, 6, 8], [16, 18, 20, 22], [30, 32, 34, 36]]


def display_table(numbers):
    indent = len(str(len(numbers)))
    print(f'{"":{indent}}', end = ' ')
    
    for row in numbers:
        for item in row:
            print(item, end=' ' )
        print() 
    

display_table(numbers)


# i couldn't get my code to run in order to get the column and row headings 