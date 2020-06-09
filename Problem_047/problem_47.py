"""
Find the first four consecutive integers to have four distinct prime 
factors each. What is the first of these numbers?
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

def next_prime(index):
    while True:
        index += 1
        if is_prime_from_list(index):
            prime_list.append(index)
            return index

def factorize_number(number):
    factors = []
    objective = number
    while not is_prime_from_list(objective):
        for i in prime_list:
            if objective%i == 0:
                # Elimina factores duplicados
                if i not in factors:
                    factors.append(i)
                objective = objective / i
                break
    return factors


# Genera los primos

index = 1
prime_list = []
for i in range(0,20000):
    index = next_prime(index)
print(f'Ultimo primo: {prime_list[len(prime_list)-1]}')


start = 100000
n_factores = 4
count = 0
while count < n_factores:
    if len(factorize_number(start)) == n_factores:
        count += 1
        #print(f'{start} --  {count}')
        if count > 1:
            print(f'{start} --  {count}')
    else:
        count = 0
    start += 1
print(f'{start - n_factores}')

