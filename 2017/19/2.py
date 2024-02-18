import string

def get_next(curr_point, direction):
    x, y = curr_point
    if direction == 'D':
        y += 1
    elif direction == 'U':
        y -= 1
    elif direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    return (x, y)

with open('input.txt') as f:
    data = [x.rstrip() for x in f.readlines()]

start_point = None
direction = 'D'

grid_points = {}
for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column in ['|', '-', '+'] or column in string.ascii_uppercase:
            grid_points[(x, y)] = column
            if y == 0:
                start_point = (x, y)

steps = 1

prev_point = None
curr_point = start_point
finished = False

while not finished:
   
    if grid_points[curr_point] in ['|', '-'] or grid_points[curr_point] in string.ascii_uppercase:
        if grid_points[curr_point] == 'F':
            finished = True
            break
        next_point = get_next(curr_point, direction)
        prev_point = curr_point
        curr_point = next_point
    else:
        assert grid_points[curr_point] == '+'
        neighbours = [
            get_next(curr_point, 'D'),
            get_next(curr_point, 'U'),
            get_next(curr_point, 'R'),
            get_next(curr_point, 'L'),
        ]

        neighbours = [None if not x in grid_points.keys() or x == prev_point else True for x in neighbours]

        assert len([x for x in neighbours if x == True]) == 1

        n_index = neighbours.index(True)
        direction = ['D', 'U', 'R', 'L'][n_index]
        
        next_point = get_next(curr_point, direction)
        prev_point = curr_point
        curr_point = next_point

    steps += 1

print(steps)
