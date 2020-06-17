"""
Find the smallest cube for which exactly five permutations of its digits are cube.
"""


# Comprueba si dos numeros tienen exactamente los mismos digitos (en otro orden)
def same_digits(n_1: int, n_2: int):
    st_1 = str(n_1)
    st_2 = str(n_2)
    if len(st_1) != len(st_2):
        return False
    for d in st_1:
        if st_2.count(d) != st_1.count(d):
            return False
    return True



found = False
n_digitos = 8
while not found:
    print(f'Analyzing {n_digitos} digits')
    # Limites
    start = int('1'+'0'*(n_digitos-1))
    stop = int('9'*n_digitos)
    start = int(round(start ** (1. / 3)))
    stop = int(round(stop ** (1. / 3)))

    cubos = []
    for i in range(start,stop+1):
        cubos.append(i ** 3)

    # Itera
    for n in range(0,len(cubos)):
        solution = [cubos[n]]
        for x in range(n+1, len(cubos)):
            if same_digits(cubos[n], cubos[x]):
                solution.append(cubos[x])
                if len(solution) == 5:
                    print(f'Min: {min(solution)}   Solution: {solution}')
                    found = True
                    break
    n_digitos += 1

