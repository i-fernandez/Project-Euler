"""
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_n_pandigital(number):
    st_num = str(number)
    if len(st_num) > 9:
        return False
    for i in range(1,len(st_num)+1):
        if str(i) not in st_num:
            return False
    return True

def is_prime_number(n):
    if n < 2:
        return False
    start = int(n**0.5)
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

# Convert a list of character into a string  
def convert(s): 
    new = ''
    for x in s: 
        new += x  
    return new 

def get_permutations(r):
    if len(r) == 1:
        return [r]
    output = []
    for i in r:
        resto = [n for n in r if n != i]
        comb = get_permutations(resto)
        for p in comb:
            l = [i] + p
            output.append(l)
    return output

prime_list = []
max_pandigital = 0
SIZE = 10
digits = [str(n) for n in range(1,SIZE)]
perm = get_permutations(digits)


for i in range(len(perm)-1,0,-1):
    n = int(convert(perm[i]))
    if n%2 != 0 and n%3 != 0 and n%5 != 0:
        if is_prime_number(n):
            if n > max_pandigital:
                max_pandigital = n
                print(f'Max pandigital: {n}')




"""
for i in range(2,987654321):
    if is_prime_from_list(i,prime_list):
        prime_list.append(i)
        if is_n_pandigital(i):
            if i > max_pandigital:
                max_pandigital = i
                print(f'Max pandigital found: {i}')


for i in range(987654321, 4231, -2):
    if is_n_pandigital(i):
        #print(f'{i} is pandigital')
        if is_prime_number(i):
            print(f'{i} is pandigital and prime')
            break
# Tope = 987654321
"""

#print(is_n_pandigital(26341))