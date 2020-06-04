"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

1x200
2x100
4x50
2x50 + 1x100
8x20
4x20 + 2x50
4x20 + 1x100
20x10
10x10 + 5x20
10x10 + 2x50
10x10 + 1x100
15x10 + 1x50

5+2+1:
40 (1)
39 (2)
38 +5+0
38+0+10
38+1+8
38+2+



2 + 1:
100 posibilidades

1:
200 posibilidades
"""

def get_coins(values, target):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        coin = values[0]
        n = int(target/coin)
        print(f'{n} monedas de {values[0]} ({coin*n} pounds)')
        return n
    suma = 0
    # Valor mas alto de moneda
    coin = values[len(values)-1]
    # Division entera
    i = int(target/coin)
    for n in range(i,0,-1):
        suma += 1
        n_monedas = target/(n*coin)
        resto = target - n_monedas*coin
        print(f'{n} monedas de {coin} ({coin*n} pounds)')
        if resto != 0:
            # Llama con una moneda menos para el resto
            suma += get_coins(values[0:len(values)-2], resto)
        else:
            print(f'Sin resto')
    
    


    return suma



    

values = [1,2,5,10,20,50,100,200]
target = 200

print(get_coins(values[0:2],target))

"""
possibilities = 0
for i in range(0,2):
    print(f'i: {i}')
    for j in range(0,i+1):
        print(f'j: {j}')
        coin = values[i]
        resto = 200
        print(f'Coin: {coin}, resto: {resto}')
        while resto != 0:
            resto -= coin
            possibilities += 1

print(possibilities)
"""