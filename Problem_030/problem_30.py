"""
1634 = 1^4 + 6^4 + 3^4 + 4^4

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

"""

def sum_fifth_power(number):
    suma = 0
    for n in str(number):
        suma += int(n)**5
    return suma == number
        


suma = 0
for i in range(10,1000000):
    if sum_fifth_power(i):
        suma += i
        print(f'Found: {i}  Sum: {suma}')
    i += 1

