#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:37:37 2020

@author: israel

What is the largest prime factor of the number 600851475143 ?

"""

from math import sqrt

VALUE = 600851475143


def get_factor(start, objective):
    for i in range(start-1,1,-1):
        if objective%i == 0:
            return i
    return 0

def is_prime(n):
    start = int((n/2)+1)
    for i in range(start, 1, -1):
        if n%i == 0:
            print(i)
            return False
        return True

def factorize(n):
    print(f'Factoring: {n}')
    objective = n
    param = int(sqrt(objective))
    factors = []

    while True:
        f = get_factor(param, objective)
        if f < 2:
            factors.append(objective)
            break
        else:
            factors.append(f)
            objective = int(objective/f)
            param = int(sqrt(objective))
    return factors

    
factors = factorize(VALUE)
fl = []
print(f'factores : {factors}')
for f in factors:
    r = factorize(f)
    for fac in r:
        fl.append(fac)
print(f'factores : {fl}')

fl2 = []
for f in fl:
    r = factorize(f)
    for fac in r:
        fl2.append(fac)
print(fl2)




