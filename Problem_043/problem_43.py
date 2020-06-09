"""
The number, 1406357289, is a 0 to 9 pandigital number 
because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from timeit import default_timer

def have_property(number):
    st_number = str(number)
    two = int(st_number[1:4])
    three = int(st_number[2:5])
    five = int(st_number[3:6])
    seven = int(st_number[4:7])
    eleven = int(st_number[5:8])
    thridteen = int(st_number[6:9])
    seventeen = int(st_number[7:10])

    if two%2 != 0:
        return False
    if three%3 != 0:
        return False
    if five%5 != 0:
        return False
    if seven%7 != 0:
        return False
    if eleven%11 != 0:
        return False
    if thridteen%13 != 0:
        return False
    if seventeen%17 != 0:
        return False
    return True
    

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

# Convert a list of character into a string  
def convert(s): 
    new = ''
    for x in s: 
        new += x  
    return new 


start_time = default_timer()
digits = [str(n) for n in range(0,10)]
suma = 0
numbers = []
for n in get_permutations(digits):
    pandi = int(convert(n))
    if have_property(pandi):
        numbers.append(pandi)
        suma += pandi

elapsed = default_timer() - start_time
print(numbers)
print(f'Suma pandis: {suma}')
print(f'Finished in {elapsed:.4} seconds')