"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""



def get_permutations(r):
    if len(r) == 1:
        return [r]
    output = []
    for i in r:
        resto = [n for n in r if n != i]
        comb = get_permutations(resto)
        for p in comb:
            l = [i] + p
            if len(l) == SIZE:
                global count
                count += 1
                if count == limit:
                    print(f'l: {l}')
                    return
            output.append(l)
    return output



if __name__ == '__main__':
    SIZE = 10
    digits = [str(n) for n in range(0,SIZE)]
    count = 0
    limit = 1000000
    get_permutations(digits)
    print(f'count {count}')
