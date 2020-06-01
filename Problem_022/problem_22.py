#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:29:21 2020

@author: israel

Using names.txt (right click and 'Save Link/Target As...'), a 
text file containing over five-thousand first names, begin by sorting 
it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to 
obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def read_data(file_name):
    names = []
    with open(file_name) as f:
        for n in f.readline().split(','):
            names.append(n.replace('"',''))
    return names

def get_name_value(name):
    total = 0
    for l in name:
        total += ord(l) - 64
    return total
    

file_name = 'p022_names.txt'
names = read_data(file_name)
names.sort()

position = 1
suma = 0
for name in names:
    # Calcula valor letras
    valor = get_name_value(name)
    # Multiplica por la posicion
    valor = valor * position
    # Suma el valor al total
    suma += valor
    position += 1

print(f'Total suma: {suma}')
