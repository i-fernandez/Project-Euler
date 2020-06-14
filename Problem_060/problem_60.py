#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:24:42 2020

@author: israel

Find the lowest sum for a set of five primes for which any two 
primes concatenate to produce another prime.

"""
from math import sqrt
#from timeit import default_timer

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
        if number_1 > last_prime or not is_present(primes, number_1):
            return False
        if number_2 > last_prime or not is_present(primes, number_2):
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


# Devuelve true si el elemento x está en arr
# busqueda binaria
def is_present(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    if x < arr[0] or x > arr[len(arr)-1]:
        return False
    
    while low <= high: 
  
        mid = (high + low) // 2
        if x == arr[mid]:
            return True
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
    # If we reach here, then the element was not present 
    return False

tope = 5
n = 100000000
primes = sieve(n)
last_prime = primes[len(primes)-1]


lowest_sum = 999999999999999999
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
            if next_id == len(primes)-1 or primes[next_id] > last_prime/1000:
                if len(prime_index) == 1:
                    break
                next_id = prime_index.pop() + 1
                prime_set.pop()
            element = primes[next_id]            
            max_val = get_concatenation(prime_set, element)
            if max_val < last_prime and concatenate_primes(prime_set, element):
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

print(prime_set)                    
print(f'--------- LOWEST: {lowest_sum} ------------------')
                    




