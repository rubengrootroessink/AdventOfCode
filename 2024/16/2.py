import heapq
import sys

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

dirs = ['E', 'N', 'W', 'S']

add_one = {
    'E': lambda n: (n[0]+1, n[1]),
    'S': lambda n: (n[0], n[1]+1),
    'W': lambda n: (n[0]-1, n[1]),
    'N': lambda n: (n[0], n[1]-1),
}

board = set()
start_node = None
end_node = None

for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column != '#':
            board.add((i, j))
        if column == 'S':
            start_node = (i, j)
        elif column == 'E':
            end_node = (i, j)

visited = {}
queue = [(0, start_node, 'E', '')]
paths = []
best_cost = sys.maxsize

while queue:
    cost, curr_node, direction, path = heapq.heappop(queue)

    if cost > best_cost:
        break

    if (curr_node, direction) in visited and visited[(curr_node, direction)] < cost:
        continue

    visited[(curr_node, direction)] = cost

    if curr_node == end_node:
        best_score = cost
        paths.append(path)

    move_one = add_one[direction](curr_node)
    if move_one in board:
        heapq.heappush(queue, (cost+1, move_one, direction, path + 'F'))
    heapq.heappush(queue, (cost+1000, curr_node, dirs[(dirs.index(direction)-1)%4], path + 'R'))
    heapq.heappush(queue, (cost+1000, curr_node, dirs[(dirs.index(direction)+1)%4], path + 'L'))

tiles = {start_node}
for p in paths:
    curr_node = start_node
    curr_direction = 'E'
    for c in p:
        if c == 'F':
            curr_node = add_one[curr_direction](curr_node)
            tiles.add(curr_node)
        elif c == 'R':
            curr_direction = dirs[(dirs.index(curr_direction)+1)%4]
        elif c == 'L':
            curr_direction = dirs[(dirs.index(curr_direction)-1)%4]

print(len(tiles))
