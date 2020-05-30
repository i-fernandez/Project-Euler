#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:26:18 2020

@author: israel

Starting in the top left corner of a 2×2 grid, and only being 
able to move to the right and down, there are exactly 6 routes 
to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

from timeit import default_timer

def next_move(row, col):
    suma = 0
    # Comprueba si es final de fila/col
    if col == size-1 or row == size-1:
        return 1
    else:
        suma += next_move(row,col+1)
        suma += next_move(row+1,col)
    return suma


    
    
if __name__ == '__main__':
    for i in range(2,16):
        start = default_timer()
        grid = i
        size = grid + 1
        paths = next_move(0, 0)
        elapsed = default_timer() - start
        print(f'Size: {grid} - Paths: {paths} in {elapsed:.2} seconds')
