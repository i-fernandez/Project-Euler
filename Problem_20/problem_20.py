#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:21:00 2020

@author: israel

Find the sum of the digits in the number 100!

"""

from math import factorial


def suma_digitos(number):
    total = 0
    for n in str(number):
        total += int(n)
    return total

def suma_factorial(number):
    return suma_digitos(factorial(number))


n = 100
print(f'Suma de digitos de factorial de {n}: {suma_factorial(n)}')

