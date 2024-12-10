from collections import defaultdict
import heapq

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

locs = defaultdict(list)
for j, row in enumerate(data):
    for i, column in enumerate(row):
        locs[int(column)].append((i, j))

resulting_paths = []

start_locs = [(x, 0, []) for x in locs[0]]
while start_locs:
    curr_loc, curr_val, path = heapq.heappop(start_locs)
    next_vals = [x for x in locs[curr_val+1] if abs(x[0]-curr_loc[0])+abs(x[1]-curr_loc[1]) == 1]

    for v in next_vals:
        if curr_val + 1 == 9:
            resulting_paths.append(path + [curr_loc, v])
        else:
            heapq.heappush(start_locs, (v, curr_val + 1, path + [curr_loc]))

print(len(resulting_paths))
