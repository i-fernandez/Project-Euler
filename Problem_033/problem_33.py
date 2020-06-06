#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:42:53 2020

@author: israel

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and 
denominator.

"""
from fractions import Fraction

def is_cancelable(num, den):
    if den%10 == 0:
        return False
    str_num = str(num)
    str_den = str(den)
    # Elimina el elemento comun
    for i in range(0,len(str_num)):
        for j in range(0,len(str_den)):
            if str_num[i] == str_den[j]:
                # Elimina el valor del numerador y denominador
                str_num = str_num[0 : i : ] + str_num[i + 1 : :]
                str_den = str_den[0 : j : ] + str_den[j + 1 : :]
                return int(str_num)/int(str_den) == num/den
    # No common elements
    return False

num_product = 1
den_product = 1
for num in range(10,101):
    for den in range(num+1,101):
        if is_cancelable(num, den):
            num_product = num_product * num
            den_product = den_product * den
            print(f'Found: {num}/{den}')
print(Fraction(num_product, den_product))

    