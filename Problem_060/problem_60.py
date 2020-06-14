#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:24:42 2020

@author: israel

Find the lowest sum for a set of five primes for which any two 
primes concatenate to produce another prime.

"""
from math import sqrt

def sieve(n,start=0):
    is_prime = [True]*n
    is_prime[:2] = [False, False]
    for i in range(2,int(sqrt(n)+1)):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index + i
    primes = []
    for i in range(n):
        if is_prime[i] and i > start:
            primes.append(i)
    return primes

# Comprueba si las concatenaciones de n con cada elemento de numbers
def concatenate_primes(numbers, n):
    for number in numbers:
        number_1 = int(str(number)+str(n))
        number_2 = int(str(n)+str(number))
        if number_1 > primes[len(primes)-1] or number_1 not in primes:
            return False
        if number_2 > primes[len(primes)-1] or number_2 not in primes:
            return False
    return True
        

def get_concatenation(numbers, n):
    #rint(f'called: {numbers}  {n}')
    st_n = str(numbers[len(numbers)-1])
    st_a = str(n)
    val1 = int(st_n + st_a)
    val2 = int(st_a + st_n)
    return max(val1, val2)

def get_prime_sum(prime_set):
    suma = 0
    for i in prime_set:
        suma += i
    return suma


tope = 5
n = 10000000
primes = sieve(n)

lowest_sum = 99999999999999999999999
for id in range(0, 1000):
    value = primes[id]
    if value not in [2,5]:
        prime_set = []
        prime_index = []
        prime_set.append(value)
        prime_index.append(id)
        print(f'First element: {value}')
        next_id = id
        suma_found = False
        while len(prime_set) < tope and not suma_found:
            next_id += 1
            #print(f'next_id: {next_id}')
            if next_id == len(primes)-1:
                if len(prime_index) == 1:
                    break
                next_id = prime_index.pop() + 1
                prime_set.pop()
                #print(f'removing {prime_set.pop()} new next_id: {next_id}')
                #print(f'New prime_set: {prime_set}')
            element = primes[next_id]
            #print(f'element: {element} at index: {next_id}')
            max_val = get_concatenation(prime_set, element)
            if max_val < primes[len(primes)-1] and concatenate_primes(prime_set, element):
                prime_set.append(element)
                prime_index.append(next_id)
                #print(f'{prime_set}')
                if len(prime_set) == tope:
                    # Escribe la suma
                    print(prime_set)
                    suma = get_prime_sum(prime_set)
                    print(f'Suma: {suma}')
                    if suma < lowest_sum:
                        lowest_sum = suma
                        print(f'--------- LOWEST: {suma} ------------------')
                        suma_found = True
                        break
        if suma_found:
            break
                    
            
                    




