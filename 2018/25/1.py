import heapq
from collections import defaultdict

with open('input.txt') as f:
    coords = [tuple([int(y) for y in x.strip().split(',')]) for x in f.readlines()]

connection_dict = defaultdict(set)
for i, c in enumerate(coords):
    for j, c_other in enumerate(coords):
        dist = sum([abs(c[k]-c_other[k]) for k in range(4)])
        if dist <= 3:
            connection_dict[i].add(j)
            connection_dict[j].add(i)

total_visited = set()
nr_constellations = 0
for key, value in connection_dict.items():
    if not key in total_visited:
        nr_constellations += 1

        to_visit = list(value)
        visited = {key}

        while to_visit:
            val = heapq.heappop(to_visit)
            visited.add(val)

            new_vals = [x for x in list(connection_dict[val]) if not x in visited]
            for new_val in new_vals:
                heapq.heappush(to_visit, new_val)
            to_visit = list(set(to_visit))

        total_visited.update(visited)

print(nr_constellations)
