import re

rep_dict = {}

with open('input.txt') as f:
    conversions, medicine = f.read().split('\n\n')

    for conversion in conversions.split('\n'):
        lhs, rhs = conversion.split(' => ')
        if lhs in rep_dict.keys():
            rep_dict[lhs].append(rhs)
        else:
            rep_dict[lhs] = [rhs]

    medicine = medicine.strip()

possible_meds = []
for key, value in rep_dict.items():
    indices = [(index.start(), index.end()) for index in re.finditer(pattern=key, string=medicine)]

    for s, e in indices:
        for item in value:
            possible_meds.append(medicine[:s] + item + medicine[e:])

print(len(set(possible_meds)))
