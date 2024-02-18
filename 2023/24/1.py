# With help from: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
# We generate 2 points on each of the lines (the current position and the next position)
# Using these points, we find the determinants using 'Given two points on each line'

low = 7
high = 27
low = 200000000000000
high = 400000000000000

def compare_stones(a, b):
    (cx_a, cy_a), (vx_a, vy_a) = a
    (cx_b, cy_b), (vx_b, vy_b) = b

    x1, y1 = cx_a, cy_a    
    x2, y2 = cx_a+vx_a, cy_a+vy_a
    x3, y3 = cx_b, cy_b
    x4, y4 = cx_b+vx_b, cy_b+vy_b

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom != 0.0:
        px = (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)
        px = px / denom
        py = (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)
        py = py / denom

        future_a = True if x2>x1 and px>x1 else True if x2<x1 and px<x1 else False
        future_b = True if x4>x3 and px>x3 else True if x4<x3 and px<x3 else False

        if low<=px<=high and low<=py<=high and future_a and future_b:
            return True

    return False
        
with open('input.txt') as f:
    hailstones = [x.split('\n')[0] for x in f.readlines()]

parsed_hailstones = []
for stone in hailstones:
    c, v = stone.split(' @ ')
    cx, cy, cz = [int(x) for x in c.split(', ')]
    vx, vy, vz = [int(x) for x in v.split(', ')]

    parsed_hailstones.append(((cx, cy), (vx, vy)))

hailstones = parsed_hailstones

result = 0
for i, stone_1 in enumerate(hailstones):
    for j, stone_2 in enumerate(hailstones[i+1:]):
        if compare_stones(stone_1, stone_2):
            result += 1

print(result)
