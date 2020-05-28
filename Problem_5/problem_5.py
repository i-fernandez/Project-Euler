"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# Primeros 4 numeros primos
primes = [2,3,5,7]

# Obtiene una lista con los factores de un numero
def get_factors(n):
    if n in primes:
        return [int(n)]
    else:
        #print(f'Calling with n={n}')
        for i in range (2,int(n)):
            if int(n)%i == 0:
                #print(f'Factor found: {i}')
                resto = get_factors(int(n)/i)
                return [*resto, *[int(i)]]
        return[int(n)]

# Devuelve un diccionario con el numer de ocurrencias de cada factor
def dict_factor(factores):
    dic = {}
    for i in factores:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

# A partir de un diccionario factor/ocurrencias, saca en mcm
def get_mcm(factores: dict):
    resultado = 1
    for i in factores.keys():
        n = i**factores[i]
        resultado = resultado * n
    return resultado



all_divisors = {}

for n in range(2,21):
    factores = dict_factor(get_factors(n))
    for f in factores.keys():
        if f in all_divisors:
            if all_divisors[f] < factores[f]:
                all_divisors[f] = factores[f]
        else:
            all_divisors[f] = factores[f]


print(f'All divisors: {all_divisors}')
mcm = get_mcm(all_divisors)

print(f'The mcm is: {mcm}')

