"""
Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
from math import sqrt

def sieve(n,start=0):
    is_prime = [True]*n
    is_prime[:2] = [False, False]
    for i in range(2,int(sqrt(n)+1)):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index + i
    primes = []
    for i in range(n):
        if is_prime[i] and i > start:
            primes.append(i)
    return primes

def is_present(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    if x < arr[0] or x > arr[len(arr)-1]:
        return False
    while low <= high: 
        mid = (high + low) // 2
        if x == arr[mid]:
            return True
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
    return False

def process_number(number: int) -> bool:
    st_number = str(number)
    for d in range(0,10):
        digit = str(d)
        if st_number.count(digit) > 1:
            prime_group = []
            # Sustituye los caracteres
            for n in range(0,10):
                # Nuevo numero
                new_number = int(st_number.replace(digit,str(n)))
                if is_present(primes, new_number):
                    prime_group.append(new_number)
            if len(prime_group) == 8:
                print(f'Group: {prime_group}')

def main(min, max):
    for number in range(min,max):
        process_number(number)       

if __name__ == '__main__':
    max = 1000000
    primes = sieve(max)
    main(100000, max)


