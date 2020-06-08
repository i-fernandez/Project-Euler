"""
What is the largest 1 to 9 pandigital 9-digit number that 
can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def is_pandigital(number):
    st_number = str(number)
    if len(st_number) != 9:
        return False
    for i in range(1,10):
        if str(i) not in st_number:
            return False
    return True

def gets_pandigital(n):
    st = ''
    index = 0
    while len(st) < 9:
        index += 1
        st += str(n * index)
    #print(f'checking: {st}')
    if is_pandigital(int(st)):
        return int(st)
    return 0

max_pan = 0
for i in range(9,10000):
    p = gets_pandigital(i)
    if p > max_pan:
        max_pan = p
        print(f'N: {i} - Pandigital: {max_pan}')
