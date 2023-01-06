#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 13:37:10 2023

@author: mackenzieporter
"""

#Exercise 4.12
#similar to the Craps simulation

"""Simulating the Tortoise and the Hare"""
import random

race_end = 70 #finish line at square 70
#function for tortoise portion of the table

def move_tortoise(tortoise):
    move1 = random.randrange(1,11)
    
    if move1 in (1,6):
        tortoise += 3 #the fast plod 
    elif move1 in (6,7): #slip
        tortoise -= 6
    elif move1 in (8,10):
        tortoise += 1

#cannot have a negative position behind the starting line 
    if tortoise < 1 :
        tortoise = 1
    
    return tortoise

def move_hare(hare):
    move2 = random.randrange(1,11)
    
    if move2 in (1,2): #sleep
        hare == 0
    elif move2 in (3,4): #the big hop
        hare += 9 
    elif move2 in (5,6): #the big slip
        hare -= 12
    elif move2 in (6,8): #small hop
        hare += 1
    elif move2 in (9,10): #small slip
        hare -= 2
        
#cannot have a negative position behind the starting line 
    if hare < 1:
        hare = 1
    
    return hare 

#positions in the race, T for tortoise, H for hare
 
def print_positions(tortoise, hare):
    for position in range(1, race_end + 1):
        if position == tortoise:
            print("T")
        elif position == hare: 
            print("H")
        elif position == tortoise and position == hare :
            print("OUCH!!!")

            
# the race 
tortoise = 1
hare = 1 

print('BANG!!!!')
print("AND THEY'RE OFF!!!!")

while tortoise < race_end and hare < race_end:
    tortoise = move_tortoise(tortoise) 
    hare = move_hare(hare)
    print_positions(tortoise, hare)
    
    

#if the race ends in a tie 
if tortoise == hare :
    print("It's a tie!")

#if the tortoise wins, or if hare wins
if tortoise > hare :
    print("TORTOISE WINS!!! YAY!!!")
else: 
    print("Hare wins.")
        
        
        
    
    


