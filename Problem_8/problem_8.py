"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?
"""
from pathlib import Path

file_name = 'numbers.txt'

numbers = []
with open(file_name,'r') as f:
    n = f.read(1)
    while n:
        if n != '\n':
            numbers.append(int(n))
        n = f.read(1)

#print(numbers)
#print(f'n: {len(numbers)}')

# Solucion chapuzera:

# Multiplica los 13 elementos de numbers a partir del elemento start
def get_multi(start, numbers):
    mult = 1
    for i in numbers[start:start+13]:
        print(i)
        mult = mult * i
    return mult

print(get_multi(0,numbers))

# Solucion un poco menos chapucera
# Comprueba si hay 0 o 1 en los 13 numeros para no evaluarlos
