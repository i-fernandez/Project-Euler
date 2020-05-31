#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:28:52 2020

@author: israel



Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

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
            if n != i and n != number:
                divisors.append(n)
        i += 1
    return divisors

# Obtiene el numero amigable de number
def get_amicable(number):
    suma = 0
    for n in get_divisors(number):
        suma += n
    return suma

amicable_list = []
for i in range(1,10000):
    if i not in amicable_list:
        am = get_amicable(i)
        am_i = get_amicable(am)
        if am_i == i and i != am:
            print(f'found amicables: {i},{am}')
            amicable_list.append(i)
            amicable_list.append(am)


print(f'Amicable list: {amicable_list}')
amicable_sum = 0
for i in amicable_list:
    amicable_sum += i
print(f'Amicable sum: {amicable_sum}')