#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:17:21 2020

@author: israel

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.
"""

from math import factorial

def is_sum_factorials(num):
    total = 0
    for n in str(num):
        total += factorial(int(n))
    return total == num


suma = 0
for i in range(10,1000000):
    if is_sum_factorials(i):
        suma += i
        print(f'found: {i} - total: {suma}')


