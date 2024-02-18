import re
import random

rev_dict = {}

with open('input.txt') as f:
    conversions, medicine = f.read().split('\n\n')

    for conversion in conversions.split('\n'):
        lhs, rhs = conversion.split(' => ')

        if rhs in rev_dict.keys():
            rev_dict[rhs].append(lhs)
        else:
            rev_dict[rhs] = [lhs]

    medicine = medicine.strip()

print(medicine)

med = medicine
counter = 0
found = False
while not found:
    choices = [x for x in rev_dict.keys() if x in med]
    if len(choices) == 0:
        if med == 'e':
            found = True
            break
        else:
            med = medicine
            counter = 0
            continue

    molecule = random.choice(choices)
    counter += 1
    replacement = random.choice(rev_dict[molecule])
    med = med.replace(molecule, replacement, 1)

print(counter)
