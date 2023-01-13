#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:05:45 2023

@author: mackenzieporter
"""

# Exercise 5.5

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a) the first half od the string using starting and ending indices 
alphabet[0:13]

# b) the first half of the string using only the ending index 
alphabet[:13]

# c) The second half of the string using starting and ending indices 
alphabet[13:26]

# d) The second half of the string using only the starting index 
alphabet[13:]

# e) Every second letter in the string starting with 'a'
alphabet[::2]

# f) The entire string in reverse 
alphabet[::-1]

# g) Every third letter of the string in reverse starting with 'z'
alphabet[::-3]
