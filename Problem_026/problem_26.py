#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:50:27 2020

@author: israel

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.

"""
#import re
from decimal import *

# devuelve el numero de decimales en el ciclo
def get_cycle(denominador):
    d = Decimal(1) / Decimal(denominador)
    print(f'number: {denominador} -> {d}')
    st = str(d).replace('0.','')
    # Quita el decimal del redondeo
    st = st[0:len(st)-1]
    #print(f'number: {st}')
    for i in range(1,len(st)):
        if st[i] == st[0]:
            resto = st.replace(st[0:i], '')
            if st[0:len(resto)] == resto:
                return i
    return len(st)
                    

"""
def get_cycle_v2(number):
    print(f'number: {number}')
    st = str(number)
    #.replace('0.','')
    print(f'st: {st}')
    regex = re.compile(r'(.+ .+)( \1)+')
    #match = regex.search(st)
    m = regex.match('001001')
    print(m)
    #print(match.group(1))
"""  
    
def main():
    getcontext().prec = 100
    max_dec = 0
    num = 0
    for i in range(1,100):
        r = get_cycle(i)
        if r > max_dec:
            max_dec = r
            num = i
            
    print(f'Best: {num}  {max_dec} dec')

def main2():
    for i in range(1,100):
        print(1/i)
    
main()
#print(get_cycle(102))
#main2()

