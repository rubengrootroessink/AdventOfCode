from collections import defaultdict

directions = ['N', 'E', 'S', 'W']

dirs = {
    'N': (0,-1),
    'E': (1,0),
    'S': (0,1),
    'W': (-1,0)
}

board = defaultdict(str)
start_pos = None

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

for j, row in enumerate(rows):
    for i, column in enumerate(row):
        board[(i,j)] = column
        if column == '^':
            start_pos = (i,j)

x, y = start_pos
dir_index = 0
locs = []
while board[(x,y)] != '':
    fwd = dirs[directions[dir_index]]
    n_x, n_y = x + fwd[0], y + fwd[1]
    if board[(n_x,n_y)] == '#':
        dir_index = (dir_index + 1) % 4
    else:
        x, y = n_x, n_y
        locs.append((x, y))

print(len(set(locs))-1)
