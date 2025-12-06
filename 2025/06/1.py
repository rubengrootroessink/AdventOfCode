import math
import re

with open('input.txt') as f:
    lines = [re.findall(r'(\S+)', l) for l in f.readlines()]

num_entries = len(lines)-1
total = 0
for i in range(len(lines[0])):
    vals = [int(lines[j][i]) for j in range(num_entries)]
    total += math.prod(vals) if lines[num_entries][i] == '*' else sum(vals)

print(total)
