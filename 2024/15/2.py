from collections import defaultdict

def tree(x, y, up):
    op = -1 if up else 1

    result_list = []
    if moving_parts[(x, y+op)] == ']':
        left, right = (x-1, y+op), (x, y+op)
    elif moving_parts[(x, y+op)] == '[':
        left, right = (x, y+op), (x+1, y+op)
    else:
        return []

    left_eval = tree(left[0], left[1], up)
    right_eval = tree(right[0], right[1], up)

    return [left, right] + left_eval + right_eval

def cycle(x, y, op, empty_board):
    new_x, new_y = x + op[0], y + op[1]
    
    # Robot pushes directly into the wall
    if empty_board[(new_x, new_y)] == '#':
        return x, y

    # Robot can move one place without touching boxes
    if moving_parts[(new_x, new_y)] == '':
        moving_parts[(x, y)] = '.'
        moving_parts[(new_x, new_y)] = '@'
        return new_x, new_y

    # Robot moves boxes in horizontal direction
    if op[1] == 0:
        curr_x, curr_y = new_x, new_y
        while moving_parts[(curr_x, curr_y)] in ['[', ']']:
            curr_x, curr_y = curr_x + op[0], curr_y + op[1]

        # Robot pushes horizontal boxes into a wall
        if empty_board[(curr_x, curr_y)] == '#':
            return x, y

        # Robot can move boxes in horizontal direction
        else:
            while (curr_x, curr_y) != (x, y):
                moving_parts[(curr_x, curr_y)] = moving_parts[(curr_x - op[0], curr_y - op[1])]
                curr_x -= op[0]
                curr_y -= op[1]
            moving_parts[(x, y)] = ''
            return new_x, new_y

    # Robot moves boxes in vertical direction
    if op[0] == 0:
        up = op[1] == -1
        old_vals = tree(x, y, up)
        new_vals = [(i, j+op[1], moving_parts[(i, j)]) for i, j in old_vals]

        if any([empty_board[(b[0], b[1])] == '#' for b in new_vals]):
            return x, y
        else:
            for v in old_vals:
                moving_parts[v] = ''
            for v in new_vals:
                i, j, k = v
                moving_parts[(i, j)] = k
            moving_parts[(x, y)] = ''
            moving_parts[(new_x, new_y)] = '@'
            return new_x, new_y
        
        return x, y

with open('input.txt') as f:
    locs, instrs = f.read().split('\n\n')

locs = locs.split('\n')
n_locs = []
for loc in locs:
    row = ''
    for item in loc:
        match item:
            case '#':
                row += '##'
            case 'O':
                row += '[]'
            case '.':
                row += '..'
            case '@':
                row += '@.'
    n_locs.append(row)

locs = n_locs

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
        elif column in ['[', ']']:
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
    if value == '[':
        count += 100*key[1]+key[0]

print(count)
