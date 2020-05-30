#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:11:13 2020

@author: israel

Work out the first ten digits of the sum of 
the following one-hundred 50-digit numbers.

"""


def read_numbers(file_name):
    numbers = []
    with open(file_name,'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n','')
            numbers.append(int(line))
            line = f.readline()
    return numbers


file = 'numbers.txt'
suma = 0
for n in read_numbers(file):
    suma += n
print(str(suma)[0:10])