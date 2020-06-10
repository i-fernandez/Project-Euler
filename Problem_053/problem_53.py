"""
How many, not necessarily distinct, values of (n|r) for 1≤ n ≤100, are greater than one-million?
"""

from math import factorial

def n_on_r(n, r):
    return int(factorial(n) / (factorial(r)*factorial(n-r)))

count = 0
for n in range(10,101):
    for r in range(1,n):
        if n_on_r(n, r) > 1000000:
            count += 1

print(f'{count}')