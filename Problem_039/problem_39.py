"""
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

20^2 + 48^2 = 52^2

"""


def triangle_count(p):
    t_count = 0
    for i in range(int(p/3), int(p/2)+1):
        cat = p - i
        for j in range(int(cat/2), i):
            p_catetos = j**2 + (cat-j)**2
            if i**2 == p_catetos:
                #print(f'P: {p} - [{i},{j},{cat-j}]')
                t_count += 1
    return t_count


max_tr = 0
for i in range(10,1001):
    n = triangle_count(i)
    if n > max_tr:
        max_tr = n
        print(f'P: {i}, {n} triangulos')

