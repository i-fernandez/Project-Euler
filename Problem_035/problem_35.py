#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:24:43 2020

@author: israel



The number, 197, is called a circular prime because all rotations 
of the digits: 197, 971, and 719, are themselves prime.

How many circular primes are there below one million?


"""

def is_prime_number(n):
    if n < 0:
        return False
    start = int(n**0.5)
    for i in range(start, 1, -1):
        if n%i == 0:
            return False
    return True

def get_rotations(num):
    str_num = str(num)
    rotations = []
    for i in range(0,len(str_num)):
        n = int(str_num[i:len(str_num)] + str_num[0:i])
        rotations.append(n)
    return rotations
        
def is_rotation_prime(numbers):
    for n in numbers:
        if not is_prime_number(n):
            return False
    return True
        

result = []
for i in range(2,1000000):
    if is_rotation_prime(get_rotations(i)):
        result.append(i)
print(result)
print(f'Number of items: {len(result)}')
