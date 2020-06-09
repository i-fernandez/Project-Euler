"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. 
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. 
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, 
for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; 
what is the value of D?

"""

def get_pentagonal(n):
    return int(n*(3*n-1)/2)

pentagonals = []
for i in range(1,10001):
    pentagonals.append(get_pentagonal(i))

less_diff = 9999999999999
gap = 1
while True:
    gap += 1
    #print(f'gap: {gap}')
    for i in range(2,len(pentagonals)-gap):
        #for j in range(i+1, i+1000):
        suma = pentagonals[i] + pentagonals[i+gap]
        diff = pentagonals[i+gap] - pentagonals[i]
        #print(f'{pentagonals[i]}:{pentagonals[i+gap]} {suma} - {diff}')
        if suma > pentagonals[len(pentagonals)-1]:
            #print(f'Suma sobrepasa ({suma}) -> break')
            break
        if diff > less_diff:
            #print(f'Diferencia sobrepasa ({diff}) -> break')
            break
        if suma in pentagonals and diff in pentagonals:
            print(f'---- suma y resta pentagonal ----')
            # Suma y resta pentagonal
            if diff < less_diff:
                less_diff = diff
                print(f'P1={i}, P2={i+gap}: diff: {diff}')
        

#print(pentagonals)