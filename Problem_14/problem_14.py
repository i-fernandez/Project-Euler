#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:18:25 2020

@author: israel

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?
"""

def get_sequence(number):
    count = 0
    n = number
    #print(n)
    while n > 1:
        count += 1
        if n%2 == 0:
            n = int(n / 2)
        else:
            n = int(3*n + 1)
        #print(n)
    return count
        

maximum = 0
number = 0
for i in range(1000000,1,-1):
    items = get_sequence(i)
    if items > maximum:
        maximum = items
        number = i
    
print(f'Number: {number}  Items: {maximum}')