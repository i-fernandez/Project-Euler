"""

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
def escribe_matriz():
    # Inicio
    start = int(size/2)
    col = start
    fil = start
    matrix[start][start] = 1
    pos = 1
    n = 2
    while True:
        # Derecha
        for i in range(0,pos):
            col += 1
            if col >= size:
                return 0
            matrix[fil][col] = n
            n += 1
        # Abajo
        for i in range(0,pos):
            fil += 1
            if fil >= size:
                return 0
            matrix[fil][col] = n
            n += 1
        # Izquierda
        pos += 1
        for i in range(0,pos):
            col -= 1
            if col < 0:
                return 0
            matrix[fil][col] = n
            n += 1
        # Arriba
        for i in range(0,pos):
            fil -= 1
            if fil < 0:
                return 0
            matrix[fil][col] = n
            n += 1
        pos += 1

def suma_diagonales():
    total = 0
    for i in range(0,size):
        total += matrix[i][i]
        total += matrix[i][size-i-1]
    # Pasa por el centro dos veces
    return total - 1

size = 1001
matrix = [[0 for col in range(size)] for row in range(size)]
escribe_matriz()
print(f'Suma diagonales: {suma_diagonales()}')