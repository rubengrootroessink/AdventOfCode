def in_range(p1, p2, edges):
    x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
    y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

    lines = []

    for h, v in edges:
        #print('\t' + str(h) + ' ' + str(v))

        if type(h) == int:
            if x_min < h < x_max and not v[0] >= y_max and not v[-1] <= y_min:
                return False
        elif type(v) == int:
            if y_min < v < y_max and not h[0] >= x_max and not h[-1] <= x_min:
                return False
    return True

with open('input.txt') as f:
    tiles = [tuple(map(int, x.split(','))) for x in f.readlines()]

edges = []

largest = 0
for i in range(len(tiles)):
    (t1x, t1y), (t2x, t2y) = tiles[i], tiles[(i+1)%len(tiles)]

    # Vertical line
    if t1y == t2y:
        edges.append((range(min(t1x, t2x), max(t1x, t2x)+1), t2y))

    # Horizontal line
    elif t1x == t2x:
        edges.append((t1x, range(min(t1y, t2y), max(t1y, t2y)+1)))

largest = 0
for i, (t1x, t1y) in enumerate(tiles):
    for (t2x, t2y) in tiles[i+1:]:
        if in_range((t1x, t1y), (t2x, t2y), edges):
            largest = max(largest, (max(t1x, t2x)+1-min(t1x, t2x))*(max(t1y, t2y)+1-min(t1y, t2y)))

print(largest)
