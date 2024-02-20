import re
import copy
import heapq

def get_neighbours(curr_node, max_x, max_y):
    result = [
        (curr_node[0]-1, curr_node[1]),
        (curr_node[0]+1, curr_node[1]),
        (curr_node[0], curr_node[1]-1),
        (curr_node[0], curr_node[1]+1),
    ]

    result = [n for n in result if 0<=n[0]<=max_x and 0<=n[1]<=max_y]
    return result

with open('input.txt') as f:
    nodes = [x.strip() for x in f.readlines()][2:]

node_pattern = r'^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$'

grid_dict = {}

max_x = 0
max_y = 0

for node in nodes:
    x, y, size, used, avail, use_per = [int(x) for x in re.match(node_pattern, node).groups()]
    
    max_x = max(max_x, x)
    max_y = max(max_y, y)

    grid_dict[(x, y)] = {
        'size': size,
        'used': used,
    }

target_node = (sorted([node[0] for node in grid_dict.keys() if node[1] == 0])[-1], 0)
empty_node = [key for key, value in grid_dict.items() if value['used'] == 0][0]
tmp_node = (target_node[0]-1, target_node[1])

initial_steps = 0 # Number

# Moving empty node to the node which is next to our target row on the top row
heap = [(empty_node, 0)]
while heap:
    curr_node, steps = heapq.heappop(heap)
    curr_size = grid_dict[curr_node]['size']

    if curr_node == tmp_node:
        initial_steps = steps
        break

    neighbours = [x for x in get_neighbours(curr_node, max_x, max_y) if grid_dict[x]['used'] <= curr_size]

    for neighbour in neighbours:
        heapq.heappush(heap, (neighbour, steps+1))

    heap = sorted(set(heap), key=lambda x: x[1])

print(initial_steps + (max_x-1)*5 + 1)
