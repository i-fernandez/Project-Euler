#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:18:35 2020

@author: israel



If the numbers 1 to 5 are written out in words: one, two, three, four, 
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

"""

to_nine = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
    }
tens = {
    0 : 'ten',
    1 : 'eleven',
    2 : 'twelve',
    3 : 'thirteen',
    4 : 'fourteen',
    5 : 'fifteen',
    6 : 'sixteen',
    7 : 'seventeen',
    8 : 'eighteen',
    9 : 'nineteen',
    }

decens = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety', 
    }



def number_to_words(number):
    str_num = str(number)
    digits = len(str_num)
    if digits == 1:
        return len(to_nine.get(number))
    if digits == 2:
        if str_num[0] == '1':
            return len(tens.get(int(str_num[1])))
        else:
            dec = len(decens.get(int(str_num[0])))
            return dec + number_to_words(int(str_num[1]))
    if digits == 3:
        cent = number_to_words(int(str_num[0]))
        h = 'hundred'
        if str_num[1] != '0' or str_num[2] != '0':
            h = h+'and'
        dec = number_to_words(int(str_num[1]+str_num[2]))
        return cent+len(h.replace(' ',''))+dec
    else:
        h = 'one thousand'
        return len(h.replace(' ',''))
        
        
    
suma = 0
for i in range(1,1001):
    val = number_to_words(i)
    suma += val
    print(f'num: {i}, letters: {val}')
print(suma)
