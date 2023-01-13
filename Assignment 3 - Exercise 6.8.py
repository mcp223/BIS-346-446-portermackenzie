#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:44:25 2023

@author: mackenzieporter
"""

# Exercise 6.8
numbers_to_words = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',
    6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 10: 'TEN', 11: 'ELEVEN',
    12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN',
    17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 30: 'THIRTY',
    40: 'FORTY', 50: 'FIFTY', 60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY',
    90: 'NINETY', 100: 'ONE HUNDRED', 200: 'TWO HUNDRED', 300: 'THREE HUNDRED',
    400: 'FOUR HUNDRED', 500: 'FIVE HUNDRED', 600: 'SIX HUNDRED', 700: 'SEVEN HUNDRED',
    800: 'EIGHT HUNDRED', 900: 'NINE HUNDRED'
    }

amount = input('Enter amount less than 1000: ')

amount_in_words = []

if amount < 1000:
    amount_in_words.append(numbers_to_words[amount])


if amount in range(1,1000):
    amount_in_words.append(numbers_to_words[amount])
    

print(f'{" "(amount_in_words)}')


# i struggled to complete this one as well

