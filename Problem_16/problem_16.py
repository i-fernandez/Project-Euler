#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:15:04 2020

@author: israel
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""

s = str(2**1000)
total = 0
for n in s:
    total += int(n)
print(f'Total sum: {total}')

