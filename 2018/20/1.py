from collections import defaultdict
import heapq

resolved = set()

conn_dict = defaultdict(set)
double_dict = defaultdict(set)

with open('input.txt') as f:
    regex = f.read()
    regex = regex[1:-2] # Split of start (^) and end ($\n) symbols

start_loc = (0, 0)

heap = [(start_loc, regex)]

while heap:
    curr_loc, rest = heapq.heappop(heap)
    resolved.add((curr_loc, rest))

    if rest == '':
        continue

    char_index = 0
    char = rest[char_index]
    
    finished = False
    while char in ['N', 'S', 'W', 'E']:
        if char == 'N':
            new_loc = (curr_loc[0], curr_loc[1]-1)
        elif char == 'S':
            new_loc = (curr_loc[0], curr_loc[1]+1)
        elif char == 'W':
            new_loc = (curr_loc[0]-1, curr_loc[1])
        elif char == 'E':
            new_loc = (curr_loc[0]+1, curr_loc[1])
        conn_dict[curr_loc].add(new_loc)
        conn_dict[new_loc].add(curr_loc)

        curr_loc = new_loc
    
        char_index += 1
        if char_index > len(rest) - 1:
            finished = True
            break
        else:
            char = rest[char_index]

    if finished:
        continue

    assert char == '('
    start_index = char_index
    curr_index = start_index + 1
    depth = 1

    char = rest[curr_index]
    split_indices = []
    while depth != 0:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == '|' and depth == 1:
            split_indices.append(curr_index-start_index-1)

        curr_index += 1
        if curr_index > len(rest) - 1:
            break
        
        char = rest[curr_index]

    next_segment = rest[start_index:curr_index][1:-1]

    segments = []

    s_index = 0
    for e_index in split_indices:
        segments.append(next_segment[s_index:e_index])
        s_index = e_index + 1
    segments.append(next_segment[s_index:])

    new_rests = [s + rest[curr_index:] for s in segments]

    for r in new_rests:
        new_val = (curr_loc, r)
        if not new_val in resolved:
            heapq.heappush(heap, new_val)

nr_nodes = len(conn_dict.keys())
flood_fill = {(0, 0)}
count = 0
while len(flood_fill) != nr_nodes:
    new_water = set()
    for k in flood_fill:
        new_water.update(conn_dict[k])
    flood_fill.update(new_water)
    count += 1

print(count)
