"""
The arithmetic sequence, 1487, 4817, 8147, in which each 
of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, 
or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def get_permutations(r):
    if len(r) == 1:
        return [r]
    output = []
    for i in range(0,len(r)):
        resto = r[0:i] + r[i+1:len(r)]
        comb = get_permutations(resto)
        for p in comb:
            l = [r[i]] + p
            output.append(l)
    return output

# Convert a list of character into a string  
def convert(s): 
    new = ''
    for x in s:
        new += str(x)  
    return new 

def is_prime_number(n):
    if n < 2:
        return False
    end = int(n**0.5)
    for i in range(2, end+1):
        if n%i == 0:
            return False
    return True

def is_sequence(terms):
    sequence = []
    for n in range(0,len(terms)):
        for o in range(n+1,len(terms)):
            dif = terms[o] - terms[n]
            if terms[o] + dif in terms:
                sequence.append(terms[n])
                sequence.append(terms[o])
                sequence.append(terms[o]+dif)
                return sequence
    return 0


for i in range(1000,10000):
    # Si es primo
    if is_prime_number(i):
        # Obtiene los digitos
        digits = []
        for d in str(i):
            digits.append(d)
        # Saca las permutaciones
        perm = [i]
        for p in get_permutations(digits):
            n = int(convert(p))
            if n not in perm and n > i and is_prime_number(n):
                perm.append(n)
        perm.sort()
        if len(perm) > 2:
            sq = is_sequence(perm)
            if sq != 0:
                print(sq)



                   



