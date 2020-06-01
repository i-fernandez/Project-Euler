"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2  
    
    Ex: 2**2 + 3**2 = 5**2


There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


for i in range(2,500):
    for j in range(i+1,500):
        resto = 1000-i-j
        if resto < j:
            break
        if resto**2 == (i**2+j**2):
            print(f'Eureka: a={i}, b={j}, c={resto}')
            a = i
            b = j
            c = resto
            break

print(f'a={a}, b={b} = c={c}')
print(f'Product = {a*b*c}')
