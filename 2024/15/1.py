from collections import defaultdict

def cycle(x, y, op, empty_board):
    curr_x, curr_y = x, y
    while True:
        if empty_board[(curr_x, curr_y)] == '#':
            return x, y
        elif moving_parts[(curr_x, curr_y)] == '':
            new_x, new_y = x + op[0], y + op[1]
            if (curr_x, curr_y) != (new_x, new_y):
                moving_parts[(curr_x, curr_y)] =  'O'
            moving_parts[(x, y)] = ''
            moving_parts[(new_x, new_y)] = '@'
            return new_x, new_y
        elif moving_parts[(curr_x, curr_y)] in ['@', 'O']:
            curr_x += op[0]
            curr_y += op[1]

with open('input.txt') as f:
    locs, instrs = f.read().split('\n\n')

locs = locs.split('\n')

x, y = None, None
empty_board = defaultdict(str)
moving_parts = defaultdict(str)
for j, row in enumerate(locs):
    for i, column in enumerate(row):
        if column == '#':
            empty_board[(i, j)] = column
        elif column == '@':
            moving_parts[(i, j)] = column
            x, y = i, j
        elif column == 'O':
            moving_parts[(i, j)] = column

instrs = instrs.replace('\n', '')

ops_dict = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1)
}

new_x, new_y = x, y
for instr in instrs:
    op = ops_dict[instr]
    new_x, new_y = cycle(new_x, new_y, op, empty_board)

count = 0
for key, value in moving_parts.items():
    if value == 'O':
        count += 100*key[1]+key[0]

print(count)
