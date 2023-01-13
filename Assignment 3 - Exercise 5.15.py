#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:29:16 2023

@author: mackenzieporter
"""

# Exercise 5.15

invoices = [(83, 'electric sander', 7, 57.98),
            (24, 'power saw', 18, 99.99),
            (7, 'sledge hammer', 11, 21.50),
            (77, 'hammer', 76, 11.99),
            (39, 'jig saw', 3, 79.50)]

# a
from operator import itemgetter

for part, desc, quant, price in sorted(invoices, key = itemgetter(1)):
    print(f'{part:}\t{desc:}\t{quant:}\t{price:}')
    
# b 
for part, desc, quant, price in sorted(invoices, key = itemgetter(3)):
    print(f'{part:}\t{desc:}\t{quant:}\t{price:}') 
    
# c
quantity = [(desc, quant) for part, desc, quant, price in invoices]

for desc, quant in sorted(quantity, key = itemgetter(1)):
    print(f'{desc:}\t{quant:}')
    
# d 
price = [(desc, quant * price) for part, desc, quant, price in invoices]

for desc, total in sorted(price, key = itemgetter(1)):
    print(f'{desc:}\t{total:}')
    
# e
price = [(desc, quant * price) for part, desc, quant, price in invoices \
         if 200 <= quant * price <= 500]

for desc, total in sorted(price, key = itemgetter(1)):
    print(f'{desc:}\t{total:}')

# f 
total = sum([(quant * price) for part, desc, quant, price in invoices])

print(f'The total for all invoices is: {total: .2f}')    
              
        