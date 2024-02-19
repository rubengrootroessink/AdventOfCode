from collections import Counter

def mht_dist(a, b):
    max_x, min_x = max(a[0], b[0]), min(a[0], b[0])
    max_y, min_y = max(a[1], b[1]), min(a[1], b[1])

    mht_dist = abs(max_x - min_x) + abs(max_y - min_y)
    return mht_dist

with open('input.txt') as f:
    coords = [tuple([int(y) for y in x.strip().split(', ')]) for x in f.readlines()]

cmp_val = 10000

lowest_x = min([x[0] for x in coords])
highest_x = max([x[0] for x in coords])
lowest_y = min([x[1] for x in coords])
highest_y = max([x[1] for x in coords])

count = 0
for y in range(lowest_y-1, highest_y+2):
    for x in range(lowest_x-1, highest_x+2):
        dists = []
        for pair in coords:
            dists.append(mht_dist((x, y), pair))
        
        if sum(dists) < cmp_val:
            count += 1

print(count)
