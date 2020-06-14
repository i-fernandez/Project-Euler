#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:40:59 2020

@author: israel
"""


def read_data(file_name):
    data = []
    with open(file_name) as f:
        line = f.readline()
        data = line.split(',')
    return data
        

def decrypt_char(value: int, key: int) -> int:
    # Convierte a entero la entrada
    value = int(value)
    # Operacion XOR
    return value ^ key


max_e = 0
file_name = 'p059_cipher.txt'
data = read_data(file_name)
# ASCII keys: 97 - 122
for key_a in range(97,123):
    for key_b  in range(97,123):
        for key_c in range(97,123):
            key = [key_a, key_b, key_c]
            data_decrypted = ''
            key_index = 0
            number_e = 0
            suma = 0
            for c in data:
                key_value = key_index%3
                res = decrypt_char(c, key[key_value])
                suma += res
                data_decrypted += chr(res)
                key_index += 1
                if chr(res) == 'e' or chr(res) == 'E':
                    number_e += 1
            if number_e > max_e:
                max_e = number_e
                print()
                print(data_decrypted)
                print(f'key: {chr(key_a)},{chr(key_b)},{chr(key_c)}')
                print(f'suma: {suma}')

#key = exp
