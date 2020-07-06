#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:26:02 2020

@author: israel
Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n 
and the ratio n/φ(n) produces a minimum.

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

def get_phi(number, factores):
    relativos = [True]*number
    relativos[0] = False
    for f in factores:
        index = 1
        while f*index < number:
            relativos[f*index] = False
            index += 1
    return sum(relativos)


def get_phi_v2(number, factores):
    relativos = 0
    index = 1
    while factores[0]*index < number:
        relativos += 1
        index += 1
    index = 1
    while factores[1]*index < number:
        n = factores[1]*index
        if n % factores[0] != 0:
            relativos += 1
        index += 1
    return number-relativos-1
    
            

# Comprueba si n1 es una permutacion de n2
def is_permutation(n1, n2):
    st_1 = str(n1)
    st_2 = str(n2)
    if len(st_1) != len(st_2):
        return False
    for ch in st_1:
        if st_2.count(ch) != st_1.count(ch):
            return False
    return True





min_ratio = 10
n = 100000
umbral = 10000000
primes = sieve(n)
print(f'Last prime: {primes[len(primes)-1]}  index: {len(primes)}')
for index in range(447,1, -1):
    #print(f'first: {primes[index]}')
    for second in range(index, len(primes)):
        number = primes[index] * primes[second]
        if number > umbral:
            break
        factores = [primes[index], primes[second]]
        phi = get_phi_v2(number, factores)
        ratio = number / phi
        if ratio < min_ratio and is_permutation(number, phi):
            min_ratio = ratio
            print(f'n: {number} ({factores})  phi(n): {phi}   ratio: {ratio}')




 

    

