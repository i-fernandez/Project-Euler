"""
Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum
"""

MAX_VAL = 100

# Suma de los cuadrados
suma_cuadrados = 0
for i in range(1,MAX_VAL+1):
    suma_cuadrados += i**2
print(f'Suma cuadrados: {suma_cuadrados}')

# Cuadrado de la suma
suma = 0
for i in range(1,MAX_VAL+1):
    suma += i
cuadrado_suma = suma**2
print(f'Cuadrado suma: {cuadrado_suma}')

# Diferencia
diff = cuadrado_suma - suma_cuadrados
print(f'Diferencia: {diff}')