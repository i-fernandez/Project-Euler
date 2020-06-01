#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:47:42 2020

@author: israel

With the following information:

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, 
        but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?

"""

days = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']

# 1 Jan 1901
jan_1_1901 = 365%7
print(f'{jan_1_1901}')

def get_days(month: int, year: int):
    if month < 1 or month > 12:
        return 0
    if month in (4,6,9,11):
        return 30
    if month in (1,3,5,7,8,10,12):
        return 31
    # Febrero
    if year % 4 == 0:
        return 29
    return 28
    


total_sundays = 0
day_1 = jan_1_1901
for i in range(1901,2001):
    for m in range(1,13):
        days = get_days(m,i)
        # Calcula el dia 1 del mes siguiente
        day_1 = (day_1 + days) % 7
        if day_1 == 6:
            total_sundays += 1
            print(f'Dia 1 de mes {m+1} año {i}: {day_1}')

print(f'Total sundays: {total_sundays}')

    

    

    

