#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:02:56 2020

@author: israel

What is the value of the first triangle number to have 
over five hundred divisors?
"""


from math import sqrt

# Obtiene todos los divisores de un numero
def get_divisors(number):
    divisors = []
    i = 1
    while i <= sqrt(number):
        if number%i == 0:
            divisors.append(int(i))
            n = int(number / i)
            if n != i:
                divisors.append(n)
        i += 1
    return len(divisors)


def get_result() :
    tr_number = 1
    count = 1
    n_div = 1
    while n_div <= 500:
        n_div = get_divisors(tr_number)
        if (n_div > 500):
            print(f'TR number: {tr_number} count: {count}  div: {n_div}')
        count += 1
        tr_number += count

get_result()
