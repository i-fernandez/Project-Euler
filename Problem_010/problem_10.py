"""
Find the sum of all the primes below two million
"""


def is_prime_from_list(n, prime_list):
    if len(prime_list) == 0:
        return True
    for p in prime_list:
        if p > n**0.5:
            return True
        if n%p == 0:
            return False
    return True



tope = 2000000
prime_list = []
suma_primos = 0
for i in range(2,tope+1):
    if is_prime_from_list(i,prime_list):
        prime_list.append(i)
        suma_primos += i
print(f'Suma: {suma_primos}')

