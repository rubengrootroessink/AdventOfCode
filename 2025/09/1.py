with open('input.txt') as f:
    tiles = [tuple(map(int, x.split(','))) for x in f.readlines()]

largest = 0
for i, (t1x, t1y) in enumerate(tiles):
    for (t2x, t2y) in tiles[i+1:]:
        largest = max(largest, (max(t1x, t2x)+1-min(t1x, t2x))*(max(t1y, t2y)+1-min(t1y, t2y)))

print(largest)
