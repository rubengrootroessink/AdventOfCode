with open('input.txt', 'r') as f:
    rows, instrs = f.read().split('\n\n')
    rows = [list(x.split('\n')[0]) for x in rows.split('\n')]
    instrs = instrs.split('\n')[0]

max_row = max([len(row) for row in rows])

maximized_rows = []
for row in rows:
    maximized_rows.append(row + [' ']*(max_row-len(row)))

rows = maximized_rows

splitted = instrs
instrs = []

while len(splitted) > 0:
    if splitted[0] in ['R', 'L']:
        instrs.append(splitted[0])
        splitted = splitted[1:]
    else:
        if not any([x in splitted for x in ['R', 'L']]):
            instrs.append(int(splitted))
            splitted = []
        else:
            index = 0
            while not splitted[index] in ['R', 'L']:
                index += 1

            instrs.append(int(splitted[0:index]))
            splitted = splitted[index:]

t_fall_off_dict = {}

# 1 --> 6
for row in range(4):
    t_fall_off_dict[('R', row, 12)] = ('L', (11-row, 15))

# 1 --> 3
for row in range(4):
    t_fall_off_dict[('L', row, 7)] = ('D', (4, 4+row))

# 1 --> 2
for column in range(8, 12):
    t_fall_off_dict[('U', -1, column)] = ('D', (4, 11-column))

# 4 --> 6
for row in range(4, 8):
    t_fall_off_dict[('R', row, 12)] = ('D', (8, 19-row))

# 3 --> 1
for column in range(4, 8):
    t_fall_off_dict[('U', 3, column)] = ('R', (column-4, 8))

# 3 --> 5
for column in range(4, 8):
    t_fall_off_dict[('D', 8, column)] = ('R', (15-column, 8))

# 5 --> 3
for row in range(8, 12):
    t_fall_off_dict[('L', row, 7)] = ('U', (7, 15-row))

# 5 --> 2
for column in range(8, 12):
    t_fall_off_dict[('D', 12, column)] = ('U', (7, 11-column))

# 6 --> 4
for column in range(12, 16):
    t_fall_off_dict[('U', 7, column)] = ('L', (19-row, 11))

# 6 --> 1
for row in range(8, 12):
    t_fall_off_dict[('R', row, 16)] = ('L', (11-row, 11))

# 6 --> 2
for column in range(12, 16):
    t_fall_off_dict[('D', 12, column)] = ('R', (column-8, 0))

# 2 --> 5
for column in range(4):
    t_fall_off_dict[('D', 8, column)] = ('U', (11, 11-column))

# 2 --> 1
for column in range(4):
    t_fall_off_dict[('U', 3, column)] = ('D', (0, 11-column))

# 2 --> 6
for row in range(4, 8):
    t_fall_off_dict[('L', row, -1)] = ('U', (11, 19-row))

# TODO, change to your specific situation (hardcoded direction changes)
fall_off_dict = {}

# 1 --> 4
for row in range(50):
    fall_off_dict[('L', row, 49)] = ('R', (149-row, 0))

# 1 --> 6
for column in range(50, 100):
    fall_off_dict[('U', -1, column)] = ('R', (column+100, 0))

# 2 --> 3
for column in range(100, 150):
    fall_off_dict[('D', 50, column)] = ('L', (column-50, 99))

# 2 --> 5
for row in range(50):
    fall_off_dict[('R', row, 150)] = ('L', (149-row, 99))

# 2 --> 6
for column in range(100, 150):
    fall_off_dict[('U', -1, column)] = ('U', (199, column-100))

# 3 --> 2
for row in range(50, 100):
    fall_off_dict[('R', row, 100)] = ('U', (49, row+50))

# 3 --> 4
for row in range(50, 100):
    fall_off_dict[('L', row, 49)] = ('D', (100, row-50))

# 4 --> 1
for row in range(100, 150):
    fall_off_dict[('L', row, -1)] = ('R', (149-row, 50))

# 4 --> 3
for column in range(50):
    fall_off_dict[('U', 99, column)] = ('R', (column+50, 50))

# 5 --> 2
for row in range(100, 150):
    fall_off_dict[('R', row, 100)] = ('L', (149-row, 149))

# 5 --> 6
for column in range(50, 100):
    fall_off_dict[('D', 150, column)] = ('L', (column+100, 49))

# 6 --> 1
for row in range(150, 200):
    fall_off_dict[('L', row, -1)] = ('D', (0, row-100))

# 6 --> 2
for column in range(50):
    fall_off_dict[('D', 200, column)] = ('D', (0, column+100))

# 6 --> 5
for row in range(150, 200):
    fall_off_dict[('R', row, 50)] = ('U', (149, row-100))

fall_dict = fall_off_dict # Change to t_ for testing purposes

x, y = rows[0].index('.'), 0
directions = ['R', 'D', 'L', 'U']
direction = 0

for instr in instrs:
    if instr == 'R':
        direction = (direction + 1) % 4
    elif instr == 'L':
        direction = (direction - 1) % 4
    else:
        for i in range(1, instr+1):
            n_direction = direction
            if directions[direction] == 'R':
                n_x, n_y = x + 1, y
                if ('R', n_y, n_x) in fall_dict.keys():
                    fall_value = fall_dict[('R', n_y, n_x)]
                    n_y, n_x = fall_value[1]
                    n_direction = directions.index(fall_value[0])

                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
                    direction = n_direction

            elif directions[direction] == 'L':
                n_x, n_y = x - 1, y
                if ('L', n_y, n_x) in fall_dict.keys():
                    fall_value = fall_dict[('L', n_y, n_x)]
                    n_y, n_x = fall_value[1]
                    n_direction = directions.index(fall_value[0])

                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
                    direction = n_direction

            elif directions[direction] == 'U':
                n_x, n_y = x, y - 1
                if ('U', n_y, n_x) in fall_dict.keys():
                    fall_value = fall_dict[('U', n_y, n_x)]
                    n_y, n_x = fall_value[1]
                    n_direction = directions.index(fall_value[0])

                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
                    direction = n_direction

            elif directions[direction] == 'D':
                n_x, n_y = x, y + 1
                if ('D', n_y, n_x) in fall_dict.keys():
                    fall_value = fall_dict[('D', n_y, n_x)]
                    n_y, n_x = fall_value[1]
                    n_direction = directions.index(fall_value[0])

                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
                    direction = n_direction

print(1000 * (y + 1) + 4 * (x + 1) + direction)
