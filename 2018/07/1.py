import re

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

pattern = r'^Step (\w) must be finished before step (\w) can begin.$'

unique_vals = set()

dep_dict = {}
for instr in instrs:
    a, b = re.match(pattern, instr).groups()

    if b in dep_dict.keys():
        dep_dict[b].add(a)
    else:
        dep_dict[b] = {a}

    unique_vals.add(a)
    unique_vals.add(b)

dep_dict = {k: v for (k, v) in sorted(dep_dict.items())}

start_val = ''.join(sorted(list(unique_vals.difference(set(dep_dict.keys())))))

order = start_val
while not len(order) == len(unique_vals):
    for k, v in dep_dict.items():
        if not k in order:
            if all([x in order for x in v]):
                order += k
                break

print(order)
