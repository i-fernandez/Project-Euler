#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:32:40 2020

@author: israel
"""
from math import sqrt
from timeit import default_timer
  

def escribe_matriz():
    # Inicio
    start = int(size/2)
    col = start
    fil = start
    pos = 2     # numero de posiciones a escribir
    n = 2       # numero a escribir
    check_number(1)
    
    ratio = 1
    while ratio > 0.1:
        # Arriba
        col += 1          # Posiciona el cursor
        for i in range(0,pos):
            fil -= 1
            n += 1
        check_number(n-1)
        fil += 1    # Corrige la fila
        # Izquierda
        for i in range(0,pos):
            col -= 1 
            n += 1
        check_number(n-1)
        # Abajo
        for i in range(0,pos):
            fil += 1 
            n += 1
        check_number(n-1)
        # Derecha
        for i in range(0,pos):
            col += 1 
            n += 1    
        side = pos+1
        check_number(n-1)
            
        pos += 2
        ratio = n_primos/n_totales
    print(f'ratio: {n_primos/n_totales}')
    print(f'Side: {side}')
        

def is_prime_number(n):
    if n < 2:
        return False
    end = int(n**0.5)
    for i in range(2, end+1):
        if n%i == 0:
            return False
    return True

def check_number(n):
    global n_totales
    global n_primos
    n_totales += 1
    #if n in primes:
    if is_prime_number(n):
        n_primos += 1


start_time = default_timer()
size = 37001  # Tamaño de la matriz virtual
n_totales = 0
n_primos = 0


escribe_matriz()
elapsed_time = default_timer() - start_time
print(f'Time elapse: {elapsed_time:.3}')


