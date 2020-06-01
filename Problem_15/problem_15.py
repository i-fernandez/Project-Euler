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
    if matrix[row][col] != 0:
        return matrix[row][col]
    # Comprueba si es final de fila/col
    if col == size-1 and row == size-1:
        matrix[row][col] = 1
        return 1
    else:
        val = 0
        if col+1 < size:
            val += next_move(row, col+1)
        if row+1 < size:
            val += next_move(row+1, col)
        matrix[row][col] = val
        return val

    
if __name__ == '__main__':
    grid = 20
    size = grid + 1
    matrix = [[0 for col in range(grid+1)] for row in range(grid+1)]
    start = default_timer()
    paths = next_move(0, 0)
    elapsed = default_timer() - start
    print(f'Size: {grid} - Paths: {paths} in {elapsed:.3} seconds')


        
