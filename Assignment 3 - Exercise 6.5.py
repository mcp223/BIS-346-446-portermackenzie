#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:47:54 2023

@author: mackenzieporter
"""

# Exercise 6.5
text = ('I was happy when I saw my mother was happy with the dinner I had made')

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else: 
        word_counts[word] = 1
        
print(f'{"WORD": <12}COUNT')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')
    
print('\nNumber of duplicate words: ' , len(word_counts))
    



        