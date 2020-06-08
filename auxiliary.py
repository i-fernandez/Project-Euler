
# Devuelve true si n es primo (sin conocimiento previo)
def is_prime_number(n):
    if n < 2:
        return False
    start = int(n**0.5)
    for i in range(start, 1, -1):
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