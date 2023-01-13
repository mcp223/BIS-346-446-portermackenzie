#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:21:55 2023

@author: mackenzieporter
"""

# Exercise 5.11
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in alphabet:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
                
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

test_sentence = 'The five boxing wizards jump quickly'
results = summarize_letters(test_sentence)

for char, count in results:
    print(f'{char}: {count}')
    
all_letters = True 

if len(results) == len(alphabet):
    for item in results:
        if item[0] not in alphabet:
            all_letters = False
            break 
else: 
    all_letters = False

if all_letters:
    print(f'"{test_sentence}" contains all the letters in the alphabet')

else:
    print(f'"{test_sentence}" does not contain all the letters in the alphabet')
    
    
    
        
    