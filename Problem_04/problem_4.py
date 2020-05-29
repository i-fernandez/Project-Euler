#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:32:24 2020

@author: israel

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(number):
    st = str(number)
    size = len(st)
    for i in range(0,int(size/2)):
        if (st[i] != st[size-i-1]):
            return False
    return True

# Comprueba si es divisible por dos numeros de tres digitos
def is_divisible(n):
    for i in range(999,100,-1):
        if n%i == 0:
            r = int(n/i)
            st = str(r)
            if len(st) == 3:
                print(f'Eureka: {n} = {i} * {r}')
                return True
    return False
    

max_val = 999*999
cont = True
while cont:
    for i in range(max_val,100,-1):
        if is_palindrome(i) and is_divisible(i):
            cont = False
            break            


