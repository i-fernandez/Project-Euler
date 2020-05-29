"""
What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?

"""

# Lee el contenido del fichero y lo devuelve como array
def read_numbers(file_name):
    numbers = []
    with open(file_name,'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n','')
            # Convierte a int
            row = [int(i) for i in line.split(' ')]
            numbers.append(row)
            line = f.readline()
    return numbers

# Multiplica los 4 elementos adyacentes de una posicion en todas direcciones
def get_multi(row, col):
    mult_f = 1
    mult_c = 1
    mult_dd = 1
    mult_di = 1
    for i in range(0,4):
        if col+i < 20:
            mult_f = mult_f * matrix[row][col+i]
        if row+i < 20:
            mult_c = mult_c * matrix[row+i][col]
        if row+i < 20 and col+i < 20:
            mult_dd = mult_dd * matrix[row+i][col+i]
        if row+i < 20 and col-i > 0:
            mult_di = mult_di * matrix[row+i][col-i]
    return max(mult_c, mult_f, mult_dd, mult_di)


matrix = read_numbers('matrix.txt')
max_val = 0
for i in range(0,20):
    for j in range(0,20):
        max_val = max(max_val, get_multi(i,j))
print(f'Max: {max_val}')