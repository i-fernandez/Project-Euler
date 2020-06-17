
# Devuelve true si n es primo (sin conocimiento previo)
def is_prime_number(n):
    if n < 2:
        return False
    end = int(n**0.5)
    for i in range(2, end+1):
        if n%i == 0:
            return False
    return True

# Devuelve true si n es primo
# Se apoya en prime_list, que contiene los primos descubiertos
# hasta el momento
def is_prime_from_list(n, prime_list):
    if len(prime_list) == 0:
        return True
    for p in prime_list:
        if n%p == 0:
            return False
    return True
prime_list = []


# Genera todas las permutaciones posibles entre los digitos de r
def get_permutations(r):
    if len(r) == 1:
        return [r]
    output = []
    for i in range(0,len(r)):
        resto = r[0:i] + r[i+1:len(r)]
        comb = get_permutations(resto)
        for p in comb:
            l = [r[i]] + p
            # No añade duplicados
            if l not in output:
                output.append(l)
    return output

# Convierte las permutaciones a enteros
def array_to_str(array: list) -> int:
    array_n = [str(n) for n in array]
    return int(''.join(array_n))

# Devuelve true si el elemento x está en arr
# busqueda binaria
def is_present(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
    if x < arr[0] or x > arr[len(arr)-1]:
        return False
    while low <= high: 
        mid = (high + low) // 2
        if x == arr[mid]:
            return True
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
    return False