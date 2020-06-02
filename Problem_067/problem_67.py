#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:45:32 2020

@author: israel
"""

def read_data(file_name):
    tree = []
    with open(file_name) as f:
        line = f.readline()
        while line:
            row = []
            for n in line.split(' '):
                row.append(int(n))
            tree.append(row)
            line = f.readline()
    return tree


file_name = 'p067_triangle.txt'
tree = read_data(file_name)

for r in range(len(tree)-2,-1,-1):
    # Itera por las filas
    for i in range(0,len(tree[r])):
        # Calcula el maximo que hay debajo
        best = max(tree[r+1][i],tree[r+1][i+1])
        # Actualiza el valor
        tree[r][i] += best
        
print(f'Best value: {tree[0][0]}')