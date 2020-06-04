#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:22:48 2020

@author: israel

We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, the 5-digit number, 
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.

"""

from timeit import default_timer

def product_pandigital(n, m, r):
    all_n = []
    for i in str(n):
        all_n.append(int(i))
    for i in str(m):
        all_n.append(int(i))
    for i in str(r):
        all_n.append(int(i))
    #print(all_n)
    if len(all_n) != 9:
        return False
    for i in range(1,10):
        if all_n.count(i) != 1:
            return False
    return True

    
start_time = default_timer()
products = []
total = 0
for a in range(1,100):
    for b in range(100,10000):
        r = a*b
        if product_pandigital(a, b, r) and r not in products:
            products.append(r)
            total += r
            #print(f'Pandigital: {a} * {b} = {r}')
print(f'Suma: {total}')
elapsed_time = default_timer() - start_time
print(f'The operation took {elapsed_time:.2} seconds')
