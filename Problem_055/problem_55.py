"""
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
How many Lychrel numbers are there below ten-thousand?
"""


def is_palindrome(number):
    st_n = str(number)
    st_r = ''
    for i in range(len(st_n)-1,-1,-1):
        st_r += st_n[i]
    return st_n == st_r

def get_reverse(number):
    st_n = str(number)
    st_r = ''
    for i in range(len(st_n)-1,-1,-1):
        st_r += st_n[i]
    return int(st_r)


def is_Lychrel(number):
    suma = number
    for i in range(1,51):
        r = get_reverse(number)
        suma += r
        if is_palindrome(suma):
            return False
        number = suma
    return True

non_lychrel = []
for i in range(2,10001):
    if  is_Lychrel(i):
        non_lychrel.append(i)

print(non_lychrel)
print(f'Non Lychrel nunmbers: {len(non_lychrel)}')

