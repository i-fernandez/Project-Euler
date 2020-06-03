"""
Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic 
expression that produces the maximum number of primes for consecutive values of n, 
starting with n=0.

"""

def cuadratic(n, a, b):
    return n**2 + n*a + b

def is_prime_number(n):
    if n < 0:
        return False
    start = int(n**0.5)
    for i in range(start, 1, -1):
        if n%i == 0:
            return False
    return True

def test_one_cycle(a, b):
    n = 0
    while True:
        v = cuadratic(n,a,b)
        if v == 0:
            return 0
        if not is_prime_number(v):
            return n+1
        n += 1
        

if __name__ == '__main__':
    max_primes = 0
    best_a = 0
    best_b = 0
    for a in range(-1000,1000):
        for b in range(1,1001):
            if is_prime_number(b):
                val = test_one_cycle(a, b)
                if val > max_primes:
                    print(f'so far: a:{a}, b:{b}, primes:{val}')
                    max_primes = val
                    best_a = a
                    best_b = b
       
    print(f'a: {best_a}, b: {best_b} - primes: {max_primes} - prod:{best_a*best_b}')




