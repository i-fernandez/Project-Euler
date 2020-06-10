"""
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def is_prime_from_list(n, prime_list):
    if len(prime_list) == 0:
        return True
    for p in prime_list:
        if n%p == 0:
            return False
    return True


def max_consecutive(n, current_max):
    max_terms = 0
    for i in range(0,len(prime_list)-current_max):
        suma = 0
        n_terms = 0
        while suma < n:
            suma += prime_list[i]
            i += 1
            n_terms += 1
            if suma == n:
                if n_terms > max_terms:
                    max_terms = n_terms
    return max_terms



prime_list = [2]
max_terms = 0
max_terms_prime = 0
for i in range(3,1000000,2):
    if is_prime_from_list(i, prime_list):
        prime_list.append(i)
        # Comprueba lo de la suma
        max_sum = max_consecutive(i, max_terms)
        if max_sum > max_terms:
            max_terms = max_sum
            max_terms_prime = i
            print(f'Prime: {max_terms_prime} ({max_terms} terms)')

print(f'Prime: {max_terms_prime} ({max_terms} terms)')


