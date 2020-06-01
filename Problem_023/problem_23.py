#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:46:54 2020

@author: israel

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.


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

def is_abundant(number):
    suma = 0
    for n in get_divisors(number):
        suma += n
    #print(f'number: {number} - sum: {suma}')
    return suma > number

# Devuelve true si number no es la suma de dos numeros abundantes
def int_no_sum(number):
    for ab in abundant_numbers:
        if ab > number:
            return True
        resto = number - ab
        if resto in abundant_numbers:
            #print(f'{number} = {ab} + {resto}')
            return False
    return True


suma = 0
abundant_numbers = []
for i in range(1,28124):
    if is_abundant(i):
        # numero abundante
        abundant_numbers.append(i)
    if int_no_sum(i):
        # no es la suma de dos numeros abundantes
        print(f'{i} no es la suma de dos abundantes')
        suma += i
        
print(f'Suma: {suma}')

        

