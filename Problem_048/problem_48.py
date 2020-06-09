"""
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

"""

suma = 0
for i in range(1,1001):
    suma += i**i

print(str(suma)[-10:])