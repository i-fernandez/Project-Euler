"""
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?
"""

# Lee el contenido del fichero y lo devuelve como lista
def read_numbers():
    numbers = []
    with open(file_name,'r') as f:
        n = f.read(1)
        while n:
            if n != '\n':
                numbers.append(int(n))
            n = f.read(1)
    return numbers

# Multiplica los 13 elementos de numbers a partir del elemento start
def get_multi(numbers):
    mult = 1
    for i in numbers:
        mult = mult * i
    return mult

file_name = 'numbers.txt'
# Obtiene los numeros del fichero
numbers = read_numbers()
maximum = 0
max_subset = []
max_i = 0
for n in range(0,988):
    subset = numbers[n:n+13]
    if (0,1) not in subset:
        # Obtiene la multiplicacion
        mult = get_multi(subset)
        if (mult > maximum):
            maximum = mult
            max_subset = subset
            max_i = n


print(f'Maximum product is {maximum}')
print(f'Max subset: {max_subset}')
print(f'Starting index: {max_i}')


