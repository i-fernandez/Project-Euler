"""
Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

"""

def is_prime_number(n):
    if n < 2:
        return False
    start = int(n**0.5)
    for i in range(start, 1, -1):
        if n%i == 0:
            return False
    return True

def all_primes(numbers):
    for i in numbers:
        if not is_prime_number(i):
            return False
    return True

def is_truncatable(number):
    if not is_prime_number(number):
        return False
    t = set()
    st_num = str(number)
    for i in range(1,len(st_num)):
        t.add(int(st_num[0:i]))
        t.add(int(st_num[i:]))
    #print(t)
    return all_primes(t)



trunc_count = 0
trunc_list = []
total = 0
index = 10
while trunc_count < 11:
    if is_truncatable(index):
        trunc_count += 1
        trunc_list.append(index)
        total += index
        print(f'Suma: {total}')
        print(trunc_list)
    index += 1

print(f'Suma: {total}')
print(trunc_list)
