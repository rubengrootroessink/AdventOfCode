# Not a fast solution (took about 3 minutes for me on the actual input)
import copy
import heapq

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

start_node = (1,0)
end_node = (len(data[0])-2, len(data)-1)

hike_points = {}
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column in ['.', '>', '<', 'v', '^']:
            hike_points[(i,j)] = column

edge_dict = {}

visited = {start_node}
heap = [(start_node, (1,1))]

cross_points = set()

while heap:
    curr_node, next_node = heapq.heappop(heap)
    s_node = curr_node
    
    length = 1

    neighbours = [
        (next_node[0]-1, next_node[1]), (next_node[0]+1, next_node[1]),
        (next_node[0], next_node[1]-1), (next_node[0], next_node[1]+1),
    ]
    neighbours = [x for x in neighbours if x in hike_points.keys() and not x == curr_node]

    while len(neighbours) == 1:
        length += 1

        curr_node = next_node
        next_node = neighbours[0]
    
        neighbours = [
            (next_node[0]-1, next_node[1]), (next_node[0]+1, next_node[1]),
            (next_node[0], next_node[1]-1), (next_node[0], next_node[1]+1),
        ]
        neighbours = [x for x in neighbours if x in hike_points.keys() and not x == curr_node]

    if len(neighbours) == 0:
        if next_node == end_node:
            edge_dict[s_node] = [(next_node, length)]

    elif len(neighbours) > 0:
        if s_node in edge_dict.keys():
            edge_dict[s_node].append((next_node, length))
        else:
            edge_dict[s_node] = [(next_node, length)]
        
        for neighbour in neighbours:
            if not next_node in cross_points:
                heapq.heappush(heap, (next_node, neighbour))

        cross_points.add(next_node)

two_way_edge_dict = copy.deepcopy(edge_dict)

for key, value in edge_dict.items():
    for v,l in value:

        if not v == end_node:
            curr_vals = two_way_edge_dict[v]
            curr_vals = curr_vals + [(key, l)]
            two_way_edge_dict[v] = list(set(curr_vals))

edge_dict = copy.deepcopy(two_way_edge_dict)

heap = [(start_node, 0, [])]

result = 0
while heap:
    curr_node, length, visited = heapq.heappop(heap)

    if curr_node == end_node:
        result = max(length, result)

    else:
        neighbours = edge_dict[curr_node]
        neighbours = [(x, y) for x, y in neighbours if not x in visited]

        for n,l in neighbours:
            heapq.heappush(heap, (n, length+l, visited + [curr_node]))

print(result)
