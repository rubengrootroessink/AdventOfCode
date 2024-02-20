import re

with open('input.txt') as f:
    nodes = [x.strip() for x in f.readlines()][2:]

node_pattern = r'^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$'

grid_dict = {}

for node in nodes:
    x, y, size, used, avail, use_per = [int(x) for x in re.match(node_pattern, node).groups()] 

    grid_dict[(x, y)] = {
        'size': size,
        'used': used,
        'avail': avail,
        'use_per': use_per,
    }

viable_pairs = 0

keys = list(grid_dict.keys())
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        a, b = grid_dict[keys[i]], grid_dict[keys[j]]
        
        if a['used'] > 0:
            if a['used'] <= b['avail']:
                viable_pairs += 1
        
        if b['used'] > 0:
            if b['used'] <= a['avail']:
                viable_pairs += 1

print(viable_pairs)
