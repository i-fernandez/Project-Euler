#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:31:10 2020

@author: israel

What is the index of the first term in the Fibonacci sequence 
to contain 1000 digits?

"""

a = 1
b = 1
index = 2
while len(str(b)) < 1000:
    index += 1
    tmp = a + b
    a = b
    b = tmp
    
print(f'index: {index} - number: {b}')