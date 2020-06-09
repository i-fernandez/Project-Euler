"""
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt

def is_prime_from_list(n):
    global prime_list
    if len(prime_list) == 0:
        return True
    for p in prime_list:
        if n%p == 0:
            return False
    return True

def next_prime():
    global index
    global prime_list
    while True:
        index += 1
        if is_prime_from_list(index):
            prime_list.append(index)
            return

def is_goldbach(number):
    for pr in prime_list:
        if pr < number:
            resto = number - pr
            if resto%2 == 0:
                sq = int(resto/2)
                # raiz perfecta
                n = int(sqrt(sq))
                if n**2 == sq:
                    #print(f'{number}: {pr} + 2* {n}^2')
                    return True
    #print(f'{number} -> Not a Goldbach')
    return False


# Genera los primos
index = 1
prime_list = []
for i in range(0,10000):
    next_prime()


for i in range(3,20000,2):
    if i not in prime_list and not is_goldbach(i):
        print(i)
        break


