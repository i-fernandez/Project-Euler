"""
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: 
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
is represented by a different number in the set.


Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	    P4,n=n2	 	        1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

"""


# Boundaries  1000 - 9999
def get_triangles(min, max):
    triangles = []
    n = 2
    while True:
        tr = n*(n+1)/2
        if tr > max:
            return triangles
        if tr >= min:
            triangles.append(int(tr))
        n += 1

def get_squares(min, max):
    squares = []
    n = 2
    while True:
        sq = n*n
        if sq > max:
            return squares
        if sq >= min:
            squares.append(int(sq))
        n += 1

def get_pentagonals(min, max):
    penta = []
    n = 2
    while True:
        pt = n*(3*n-1)/2
        if pt > max:
            return penta
        if pt >= min:
            penta.append(int(pt))
        n += 1

def get_hexagonal(min, max):
    hexa = []
    n = 2
    while True:
        hx = n*(2*n-1)
        if hx > max:
            return hexa
        if hx >= min:
            hexa.append(int(hx))
        n += 1

def get_hepta(min, max):
    hepta = []
    n = 2
    while True:
        hp = n*(5*n-3)/2
        if hp > max:
            return hepta
        if hp >= min:
            hepta.append(int(hp))
        n += 1

def get_octo(min, max):
    octo = []
    n = 2
    while True:
        oc = n*(3*n-2)
        if oc > max:
            return octo
        if oc >= min:
            octo.append(int(oc))
        n += 1

# Devuelve los numeros cuyos dos primeros digitos
# coinciden con los dos pasados por parametro
def numbers_matching(numbers: list, two_digits: str):
    match = []
    for n in numbers:
        if str(n)[:2] == two_digits:
            match.append(n)
    return match

# Comprueba si la lista está entera y es circular
def is_finished(found: list, last: int):
    # Comprueba si los dos ultimos digitos de last son igual a los dos primeros de found[0]
    if str(last)[2:] != str(found[0])[:2]:
        return False

    for e in found:
        if e == 0:
            return False
    return True


def search_triangle(found: list):
    for element in tr:
        found[0] = element
        last_two = str(element)[2:]
        search_all(found, last_two)
        found[0] = 0
   

def search_type(found: list, first_digits: str, position: int, number_list: list):
    if found[position] == 0:
        for element in numbers_matching(number_list, first_digits):
            found[position] = element
            if is_finished(found, element):
                print(f'Solution: {found}')
                suma = 0
                for s in found:
                    suma += s
                print(f'Suma: {suma}')
            last_two = str(element)[2:]
            search_all(found, last_two)
            found[position] = 0
    

def search_all(found: list, first_digits: str):
    # Squares
    search_type(found, first_digits, 1, sq)
    # Pentagonal
    search_type(found, first_digits, 2, pt)
    # Hexagonal
    search_type(found, first_digits, 3, hx)
    # Heptagonal
    search_type(found, first_digits, 4, hp)
    # Octagonal
    search_type(found, first_digits, 5, oc)


tr = get_triangles(1000, 9999)
sq = get_squares(1000,9999)
pt = get_pentagonals(1000,9999)
hx = get_hexagonal(1000,9999)
hp = get_hepta(1000,9999)
oc = get_octo(1000,9999)

found = [0]*6
search_triangle(found)


