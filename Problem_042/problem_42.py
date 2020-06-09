

def get_n_triangle(max):
    tr = []
    for i in range(1,max+1):
        tr.append(int(0.5*i*(i+1))) 
    return tr

def word_to_int(word):
    suma = 0
    for l in word:
        suma += (ord(l)-64)
    return suma

def read_data(file_name):
    output = []
    with open(file_name) as f:
        words = f.readline().split(',')
        for w in words:
            output.append(w.replace('"',''))
    return output
        


file_name = 'p042_words.txt'
words = read_data(file_name)
triangles = get_n_triangle(200)
tr_words = []
for w in words:
    s = word_to_int(w)
    if s in triangles:
        tr_words.append(w)

print(f'Triangle words: {len(tr_words)}')
