from collections import Counter

def mht_dist(a, b):
    max_x, min_x = max(a[0], b[0]), min(a[0], b[0])
    max_y, min_y = max(a[1], b[1]), min(a[1], b[1])

    mht_dist = abs(max_x - min_x) + abs(max_y - min_y)
    return mht_dist

with open('input.txt') as f:
    coords = [tuple([int(y) for y in x.strip().split(', ')]) for x in f.readlines()]

lowest_x = min([x[0] for x in coords])
highest_x = max([x[0] for x in coords])
lowest_y = min([x[1] for x in coords])
highest_y = max([x[1] for x in coords])

result_dict = {}

for i, coord in enumerate(coords):
    result_dict[coord] = str(i)

for y in range(lowest_y-1, highest_y+2):
    for x in range(lowest_x-1, highest_x+2):

        dists = []
        for pair in coords:
            dists.append(mht_dist((x, y), pair))
        
        occ = Counter(dists)
        lowest = min(dists)

        if occ[lowest] == 1:
            result_dict[(x, y)] = dists.index(lowest)
        else:
            result_dict[(x, y)] = '.'

infinite_nums = set()
for y in [lowest_y-1, highest_y+1]:
    for x in range(lowest_x-1, highest_x+2):
        val = result_dict[(x, y)]
        if val != '.':
            infinite_nums.add(val)

for x in [lowest_x-1, highest_x+1]:
    for y in range(lowest_y-1, highest_y+2):
        val = result_dict[(x, y)]
        if val != '.':
            infinite_nums.add(val)

infinite_nums = list(infinite_nums)

largest = 0
for i, coord in enumerate(coords):
    if not i in infinite_nums:
        largest = max(largest, len([x for x in result_dict.values() if x == i]))

print(largest)
