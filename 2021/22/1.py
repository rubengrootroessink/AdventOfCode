from itertools import product
import re

def reduce_list(low, high):
    return list(range(max(low, -50), min(high+1, 50)))

instrs = []
with open('input.txt') as f:
    instrs = [x.split('\n')[0].split(' ') for x in f.readlines()]

on = set()
for op, value in instrs:
    dx, dy, dz = [[int(y) for y in x.split('..')] for x in re.split(',?[xyz]=', value)[1:]]
    dx = reduce_list(dx[0], dx[1])
    dy = reduce_list(dy[0], dy[1])
    dz = reduce_list(dz[0], dz[1])
    
    p = set(product(dx, dy, dz))
    if op == 'on':
        on = on.union(p)
    else:
        on = on - p
    
print(len(on))
