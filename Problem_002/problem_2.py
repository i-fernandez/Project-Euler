#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:27:21 2020

@author: israel

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, 
find the sum of the even-valued terms.

"""

MAX_VAL = 4000000

def fibonacci():
    suma = 0
    a = 1
    b = 1
    while a+b < MAX_VAL:
        tmp = a + b
        a = b
        b = tmp
        if b%2 == 0:
            suma += b
    return suma
    
print(fibonacci())
