"""
How many n-digit positive integers exist which are also an nth power?
"""


def get_power_digits(n: int):
    total_numbers = 0
    current = 1
    while True:
        power = current ** n_digits
        digit_count = len(str(power))
        if digit_count == n_digits:
            total_numbers += 1
        elif digit_count > n_digits:
            print(f'{n_digits} : {total_numbers}')
            return total_numbers
        current += 1



total = 0
n_digits = 1
go_on = True
while go_on:
    r = get_power_digits(n_digits)
    if r > 0:
        total += r
        n_digits += 1
    else:
        go_on = False
print(f'Total numbers: {total}')

