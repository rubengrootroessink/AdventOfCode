from collections import defaultdict

def empty():
    return '.'

def turn(curr_dir, turn_right=True):
    directions = ['U', 'R', 'D', 'L']
    
    curr_index = directions.index(curr_dir)

    if turn_right:
        next_index = (curr_index + 1) % 4
    else:
        next_index = (curr_index - 1) % 4

    return directions[next_index]

def move(curr_loc, direction):
    if direction == 'U':
        next_loc = (curr_loc[0], curr_loc[1]-1)
    elif direction == 'R':
        next_loc = (curr_loc[0]+1, curr_loc[1])
    elif direction == 'D':
        next_loc = (curr_loc[0], curr_loc[1]+1)
    elif direction == 'L':
        next_loc = (curr_loc[0]-1, curr_loc[1])
    return next_loc


with open('input.txt') as f:
    grid = [x.strip() for x in f.readlines()]

grid_size = len(grid)
offset = (grid_size-1) // 2

infected = defaultdict(empty)

for j, row in enumerate(grid):
    for i, column in enumerate(row):
        if column == '#':
            infected[(i-offset, j-offset)] = '#'

curr_loc = (0, 0)
curr_dir = 'U'

bursts = 0
for i in range(10000):
    if infected[curr_loc] == '.':
        curr_dir = turn(curr_dir, turn_right=False)
        infected[curr_loc] = '#'
        bursts += 1

    elif infected[curr_loc] == '#':
        curr_dir = turn(curr_dir, turn_right=True)
        infected[curr_loc] = '.'

    curr_loc = move(curr_loc, curr_dir)

print(bursts)
