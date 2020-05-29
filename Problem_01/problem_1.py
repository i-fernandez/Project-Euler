#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:10:41 2020

@author: israel

Find the sum of all the multiples of 3 or 5 below 1000.

"""


sum = 0
for i in range(3,1000):
    if i%3 == 0 or i%5 == 0:
        sum += i        
print(sum)    
    