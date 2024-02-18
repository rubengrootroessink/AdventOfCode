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

result = 0
heap = [(start_node, [])]
while heap:
    (i, j), visited = heapq.heappop(heap)

    if (i, j) == end_node:
        result = max(len(visited), result)
        continue

    neighbours = [
        (i-1,j),(i+1,j),
        (i,j-1),(i,j+1),
    ]
    
    column = hike_points[(i,j)]
    if column == '<':
        neighbours = [neighbours[0]]
    elif column == '>':
        neighbours = [neighbours[1]]
    elif column == '^':
        neighbours = [neighbours[2]]
    elif column == 'v':
        neighbours = [neighbours[3]]
    
    neighbours = [x for x in neighbours if x in hike_points.keys() and not x in visited]

    for neighbour in neighbours:
        heapq.heappush(heap, (neighbour, visited + [(i,j)]))

print(result)
