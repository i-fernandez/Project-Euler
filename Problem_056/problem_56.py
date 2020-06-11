"""
Considering natural numbers of the form, ab, 
where a, b < 100, what is the maximum digital sum?
"""

def count_digits(a, b):
    st_n = str(a**b)
    suma = 0
    for d in st_n:
        suma += int(d)
    return suma

max_sum = 0
for a in range(10,101):
    for b in range(10,101):
        sum_digits = count_digits(a, b)
        if sum_digits > max_sum:
            max_sum = sum_digits

print(f'Max: {max_sum}')


