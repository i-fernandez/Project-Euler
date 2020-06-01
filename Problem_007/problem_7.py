"""
What is the 10 001st prime number?
"""



def is_prime(n):
    start = int(n/2)
    for i in range(start, 1, -1):
        if n%i == 0:
            return False
    return True


def is_prime_from_list(n, prime_list):
    if len(prime_list) == 0:
        return True
    for p in prime_list:
        if n%p == 0:
            return False
    return True


tope = 10001
prime_list = []
prime_number = 0
n = 1
while prime_number < tope:
    n += 1
    if is_prime_from_list(n,prime_list):
        prime_list.append(n)
        prime_number += 1
        #print(f'Prime {prime_number}: {n}')

print(prime_list)
print(f'{tope} prime number is: {n}')





