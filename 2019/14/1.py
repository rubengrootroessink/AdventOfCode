# Inspired by others
from collections import defaultdict
import random

with open('input.txt') as f:
    convs = [x.strip() for x in f.readlines()]

conv_dict = {}
for conv in convs:
    lhs, rhs = conv.split(' => ')
    quantity, item = rhs.split(' ')
    quantity = int(quantity)

    sub_elements = []
    for e in lhs.split(', '):
        q, i = e.split(' ')
        q = int(q)
        sub_elements.append((q, i))

    assert not item in conv_dict.keys() # Checking some asserts for full input
    conv_dict[item] = (quantity, sub_elements)

def get_fuel(fuel_amount):
    need = {'FUEL': fuel_amount}
    have = defaultdict(int)

    while list(need.keys()) != ['ORE']:

        to_be_converted = [x for x in need.keys() if x != 'ORE']
        ran_val = random.choice(to_be_converted)

        quantity, sub_elements = conv_dict[ran_val]

        quotient, remainder = divmod(need[ran_val], quantity)

        if remainder != 0:
            have[ran_val] = quantity - remainder
            quotient += 1

        del need[ran_val]

        for q, i in sub_elements:
            need[i] = need.get(i, 0) + quotient * q - have[i]
            del have[i]

    return need['ORE']

print(get_fuel(1))
