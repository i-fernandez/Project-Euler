"""
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


def is_prime_number(n):
    if n < 2:
        return False
    start = int(n**0.5)
    for i in range(start, 1, -1):
        if n%i == 0:
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


max_pandigital = 0

for size in range(10,1,-1):
    digits = [str(n) for n in range(1,size)]
    perm = get_permutations(digits)
    
    
    for i in range(len(perm)-1,0,-1):
        n = int(convert(perm[i]))
        if n%2 != 0 and n%3 != 0 and n%5 != 0:
            if is_prime_number(n):
                if n > max_pandigital:
                    max_pandigital = n
                    print(f'Max pandigital: {n}')

