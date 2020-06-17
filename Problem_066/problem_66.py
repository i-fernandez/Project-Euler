"""
Find the value of D ≤ 1000 in minimal solutions of x 
for which the largest value of x is obtained.
"""
from math import sqrt

def get_Diophantine(d: int):
    # x^2 - d * y^2 =  1
    for y in range(0,20000000):
        y += 1
        r = 1 + d*(y**2)
        #print(f'x:{int(sqrt(r))} D:{d} y:{y}')
        if is_perfect_square(r):
            return int(sqrt(r))
    return 0


def is_perfect_square(number):
    root = sqrt(number)
    return int(root + 0.5) ** 2 == number





max_x = 0
max_d = 0
not_solved = []
for d in range(1,1001):
    if not is_perfect_square(d):
        r = get_Diophantine(d)
        print(f'd = {d}   x = {r}')
        if r == 0:
            print(f'---------- {d} -----------')
            not_solved.append(d)
        if r > max_x:
            max_x = r
            max_d = d
            print(f'found max: {max_x}')


print(f'Max x: {max_x} at d: {max_d}')
print(f'Not solved: {not_solved}')

    


