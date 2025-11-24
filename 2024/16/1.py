import heapq

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

visited = {(start_node, 'E')}
queue = [(0, start_node, 'E')]

while queue:
    cost, curr_node, direction = heapq.heappop(queue)

    if curr_node == end_node:
        print(cost)
        break

    turns = [(curr_node, x) for x in dirs if not (curr_node, x) in visited and add_one[x](curr_node) in board]
    
    for new_node, new_direction in turns:
        heapq.heappush(queue, (cost+1000, new_node, new_direction))
        visited.add((new_node, new_direction))

    move_one = add_one[direction](curr_node)
    if move_one in board and not move_one in visited:
        heapq.heappush(queue, (cost+1, move_one, direction))
        visited.add((move_one, direction))
