"""
In the first one-thousand expansions, 
how many fractions contain a numerator with more digits than the denominator?
"""
from fractions import Fraction,Decimal
import re

def next_term(expr: str, n: int):
    insert = '+Fraction(Fraction(1,2))'
    head = expr[0:len(expr)-(2*n)+3]
    tail = expr[len(expr)-(2*n)+3:len(expr)]
    new_exp = head + insert + tail
    #print(new_exp)
    return new_exp

def numerator_more_digits(f: Fraction):
    st_n = str(f.numerator)
    st_d = str(f.denominator)
    return len(st_n) > len(st_d)

def evaluate_sub(expression: str):
    p = re.compile('(\S*)')


first = '1+Fraction(1,2)'
term = first

count = 0
for i in range(2, 3):
    term = next_term(term,i)
    
    """
    # Es necesaria una funcion que evalue las expresiones, delimitando por Fraction()
    number = eval(term)
    res = Fraction(str(number))
    if numerator_more_digits(res):
        count += 1
    """

exp = '1+Fraction(1,2+Fraction(Fraction(1,2)))'
p = re.findall('Fraction\([\d,/+]*\)',exp)
print(p[0])
res = eval(p[0])
print(res)

"""
exp = exp.replace(p[0],str(res))
print(exp)
p = re.findall('Fraction\([\d,/+]*\)',exp)
res = eval(p[0])
print(res)
exp = exp.replace(p[0],str(res))
print(exp)
p = re.findall('Fraction\([\d,/+]*\)',exp)
print(p[0])
res = eval(p[0])
#print(res)
"""

#print(p)
#print(p.findall(exp))
#print(p.match(exp))


#print(f'Cumplen: {count}')

