import sys
import copy
import heapq
from collections import defaultdict

def get_neighbours(node):
    return [
        (node[0]-1, node[1]),
        (node[0]+1, node[1]),
        (node[0], node[1]-1),
        (node[0], node[1]+1),
    ]

def ret_val():
    return '#'

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

board = defaultdict(ret_val)
numbered_points = {}

for j, row in enumerate(data):
    for i, column in enumerate(row):
        new_elem = column
        if new_elem.isdigit():
            new_elem = int(new_elem)
            numbered_points[(i, j)] = new_elem
        if new_elem != '#':
            board[(i, j)] = new_elem

graph = {}

for key, value in numbered_points.items():
    graph_key_dict = {}

    flood_board = copy.deepcopy(board)
    steps = 1

    neighbours = [x for x in get_neighbours(key) if flood_board[x] != '#']
    flood_board[key] = '#'
    
    while neighbours != []:

        new_neighbours = []
        for node in neighbours:

            if type(flood_board[node]) == int:
                graph_key_dict[flood_board[node]] = steps
            
            new_neighbours += [x for x in get_neighbours(node) if flood_board[x] != '#']

            flood_board[node] = '#'

        neighbours = list(set(new_neighbours))
        steps += 1

    graph[value] = graph_key_dict

start_val = 0
heap = [(start_val, [start_val], 0)]

min_steps = sys.maxsize

while heap:

    curr_node, path, nr_steps = heapq.heappop(heap)

    if list(sorted(path)) == list(range(0, len(graph))):
        min_steps = min(min_steps, nr_steps + graph[path[-1]][0])

    for next_node, dist in graph[curr_node].items():
        if not next_node in path:
            heapq.heappush(heap, (next_node, path + [next_node], nr_steps + dist))

print(min_steps)
