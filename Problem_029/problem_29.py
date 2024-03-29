"""
How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

"""

values = set()
for a in range(2,101):
    for b in range(2,101):
        values.add(a**b)

print(f'number or elements: {len(values)}')
