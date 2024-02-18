import re

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

pattern = r'^position=<\s*(\-?\d+),\s*(\-?\d+)> velocity=<\s*(\-?\d+),\s*(\-?\d+)>$'

points = []

for line in lines:
    x, y, vx, vy = [int(p) for p in re.match(pattern, line).groups()]
    points.append((x, y, vx, vy))

while max([p[1] for p in points]) - min([p[1] for p in points]) > 10:
    points = [(p[0]+p[2], p[1]+p[3], p[2], p[3]) for p in points]

min_x = min([p[0] for p in points])
max_x = max([p[0] for p in points])

min_y = min([p[1] for p in points])
max_y = max([p[1] for p in points])

final_points = [(p[0], p[1]) for p in points]

for y in range(min_y, max_y+1):
    row = []
    for x in range(min_x, max_x + 1):
        if (x, y) in final_points:
            row.append('#')
        else:
            row.append('.')
    print(''.join(row))
