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
            if directions[direction] == 'R':
                n_x, n_y = x + 1, y
                if n_x >= len(rows[n_y]) or rows[n_y][n_x] == ' ':
                    n_x = 0
                    while rows[n_y][n_x] == ' ':
                        n_x = n_x + 1
                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
            elif directions[direction] == 'L':
                n_x, n_y = x - 1, y
                if n_x < 0 or rows[n_y][n_x] == ' ':
                    n_x = len(rows[n_y]) - 1
                    while rows[n_y][n_x] == ' ':
                        n_x = n_x - 1
                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
            elif directions[direction] == 'U':
                n_x, n_y = x, y - 1
                if n_y < 0 or rows[n_y][n_x] == ' ':
                    n_y = len(rows) - 1
                    while rows[n_y][n_x] == ' ':
                        n_y = n_y - 1
                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y
            elif directions[direction] == 'D':
                n_x, n_y = x, y + 1
                if n_y >= len(rows) or rows[n_y][n_x] == ' ':
                    n_y = 0
                    while rows[n_y][n_x] == ' ':
                        n_y = n_y + 1
                if not rows[n_y][n_x] == '#':
                    x, y = n_x, n_y

print(1000 * (y + 1) + 4 * (x + 1) + direction)
