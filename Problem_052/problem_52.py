"""
Find the smallest positive integer, x, 
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits
"""

def same_digits(n_1, n_2):
    st_1 = str(n_1)
    st_2 = str(n_2)
    if len(st_1) != len(st_2):
        return False
    list_1 = []
    list_2 = []
    for s in st_1:
        list_1.append(s)
    for s in st_2:
        list_2.append(s)
    # Ordena
    list_1.sort()
    list_2.sort()
    # Comprueba que son iguales
    return list_1 == list_2

def check_number(n):
    for i in range(2, 7):
        if not same_digits(n, n*i):
            return False
    return True
    


for i in range(100, 1000000):
    if check_number(i):
        print(i)
        break

