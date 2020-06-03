#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:50:27 2020

@author: israel

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.

"""
#import re
from decimal import Decimal,getcontext

# devuelve el numero de decimales en el ciclo
def get_cycle(denominador):
    d = Decimal(1) / Decimal(denominador)
    print(f'number: {denominador} -> {d}')
    st = str(d).replace('0.','')
    # Quita el decimal del redondeo
    st = st[0:len(st)-1]
    #print(f'number: {st}')
    for i in range(len(st)-1,1,-1):
        #if st[i] == st[0]:
        print(f'i: {i} - val: {st[i]}')
        if st[i] == st[len(st)-1]:
            print(f'Iguales')
            
            resto = st.replace(st[i:len(st)-1], '')
            print(f'resto: {resto}')
            if st[0:len(resto)] == resto:
                return i
    return len(st)
                    


    
def main():
    #getcontext().prec = 100
    max_dec = 0
    num = 0
    for i in range(1,100):
        r = get_cycle(i)
        if r > max_dec:
            max_dec = r
            num = i
            
    print(f'Best: {num}  {max_dec} dec')

def main2():
    getcontext().prec = 100
    get_cycle(6)
    #for i in range(1,100):
    #    print(1/i)
    

getcontext().prec = 100
#main()
print(get_cycle(6))


