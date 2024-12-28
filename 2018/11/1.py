from collections import defaultdict
from functools import cache
import math

def pwr_lvl(x, y, serial_num):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_num
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    
    return power_level

@cache
def prefix_sum(x, y):
    if (x, y) == (0, 0):
        return power_levels[(0, 0)]
    elif y == 0:
        return sum([power_levels[(i, y)] for i in range(0, x+1)])
    elif x == 0:
        return sum([power_levels[(x, j)] for j in range(0, y+1)])
    else:
        x_vals = sum([power_levels[(i, y)] for i in range(0, x+1)])
        y_vals = sum([power_levels[(x, j)] for j in range(0, y)]) # Remove one, to ensure no overlap
        return prefix_sum(x-1, y-1) + x_vals + y_vals

with open('input.txt') as f:
    serial_num = int(f.read())

power_levels = {}
for y in range(0, 300):
    for x in range(0, 300):
        power_levels[(x, y)] = pwr_lvl(x, y, serial_num)

cells = defaultdict(int)
for y in range(0, 300):
    for x in range(0, 300):
        cells[(x, y)] = prefix_sum(x, y)

max_val = 0
loc_x, loc_y = None, None

size = 3
for y in range(0, 300-size):
    for x in range(0, 300-size):
        A = cells[(x-1, y-1)]
        B = cells[(x+size, y-1)]
        C = cells[(x-1, y+size)]
        D = cells[(x+size, y+size)]

        val = D - B - C + A

        if val > max_val:
            max_val = val
            loc_x, loc_y = x, y

print(str(loc_x+1) + ',' + str(loc_y+1)) # Index in assignment starts with 1, not 0
