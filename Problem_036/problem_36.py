#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:44:22 2020

@author: israel

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

"""

def is_palindrome(number):
    st = str(number)
    size = len(st)
    for i in range(0,int(size/2)):
        if (st[i] != st[size-i-1]):
            return False
    return True


def pal_both_bases(number):
    b2 = bin(number)[2:]
    return is_palindrome(number) and is_palindrome(b2)
   

suma = 0
for i in range(1,1000000):
    if pal_both_bases(i):
        suma += i
        
print(f'Sum: {suma}')
