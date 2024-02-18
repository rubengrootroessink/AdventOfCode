import math
from itertools import combinations

with open('input.txt') as f:
    packages = [int(x.strip()) for x in f.readlines()]

total_weight = sum(packages)
split_weight = total_weight // 4

min_middle_size = min([i for i in range(1, len(packages)) if sum(packages[-i:]) >= split_weight]) # As we can expect the lines sorted

possible_vals = []
for i in range(min_middle_size, (len(packages) // 4) + 1):
    for combo in combinations(packages, i):
        if sum(combo) == split_weight:
            possible_vals.append((len(combo), combo))

num_packages_first_combo = possible_vals[0][0]
print(min([math.prod(j[1]) for j in possible_vals if j[0] == num_packages_first_combo]))
