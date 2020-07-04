#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:22:37 2020

@author: israel

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

"""

from math import sqrt
from timeit import default_timer


# Devuelve una lista de factores unicos de number
def get_factores(number):
    factores = []
    resto = number
    for i in range(2,int(sqrt(number)+1)):
        if resto % i == 0:
            factores.append(i)
            while resto % i == 0:
                resto = resto / i
            if resto == 1:
                return factores
    factores.append(int(resto))
    return factores
 

def get_relative_primes(number):
    factores = get_factores(number)
    relativos = [True]*number
    relativos[0] = False
    for f in factores:
        index = 1
        while f*index < number:
            relativos[f*index] = False
            index += 1
    return sum(relativos)


# Calcula el ratio n / phi(n)
def get_euler_ratio(n):
    return n / get_relative_primes(n)


max_ratio = 0
max_time = 0
for i in range(2,1000001):
    start = default_timer()
    ratio = get_euler_ratio(i)
    elapsed = default_timer() - start
    if elapsed > max_time:
        max_time = elapsed
        print(f'n: {i} ratio {ratio}   {elapsed:.3}')
    if ratio > max_ratio:
        max_ratio = ratio
        print(f'MAX   n: {i} ratio {ratio}  {elapsed:.3}')
        
"""
MAX TIME: 232434 0.104 sec.
"""