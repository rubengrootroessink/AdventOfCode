import re

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

pattern = r'^position=<\s*(\-?\d+),\s*(\-?\d+)> velocity=<\s*(\-?\d+),\s*(\-?\d+)>$'

points = []

for line in lines:
    x, y, vx, vy = [int(p) for p in re.match(pattern, line).groups()]
    points.append((x, y, vx, vy))

count = 0
while max([p[1] for p in points]) - min([p[1] for p in points]) > 10:
    points = [(p[0]+p[2], p[1]+p[3], p[2], p[3]) for p in points]
    count += 1

print(count)
