from collections import Counter

def up(node, c):
    return ((node[0], node[1]-1), 'up', c)

def down(node, c):
    return ((node[0], node[1]+1), 'down', c)

def left(node, c):
    return ((node[0]-1, node[1]), 'left', c)

def right(node, c):
    return ((node[0]+1, node[1]), 'right', c)

with open('input.txt') as f:
    board = [x.rstrip() for x in f.readlines()]

loc_dict = {}
start_locs = []
for j, row in enumerate(board):
    for i, column in enumerate(row):

        if column in ['v', '^', '|']:
            loc_dict[(i, j)] = {'up': lambda x, y: up(x, y), 'down': lambda x, y: down(x, y)}
            
            if column == '^':
                start_locs.append(((i, j), 'up', 0))
            elif column == 'v':
                start_locs.append(((i, j), 'down', 0))

        elif column in ['>', '<', '-']:
            loc_dict[(i, j)] = {'left': lambda x, y: left(x, y), 'right': lambda x, y: right(x, y)}
            
            if column == '>':
                start_locs.append(((i, j), 'right', 0))
            elif column == '<':
                start_locs.append(((i, j), 'left', 0))

        elif column in ['/', '\\']:
            if column == '/':
                loc_dict[(i, j)] = {
                    'up': lambda x, y: right(x, y),
                    'down': lambda x, y: left(x, y),
                    'left': lambda x, y: down(x, y),
                    'right': lambda x, y: up(x, y)
                } 
            elif column == '\\':
                loc_dict[(i, j)] = {
                    'up': lambda x, y: left(x, y),
                    'down': lambda x, y: right(x, y),
                    'left': lambda x, y: up(x, y),
                    'right': lambda x, y: down(x, y)
                } 
        
        elif column in ['+']:
            loc_dict[(i, j)] = {
                'up': lambda x, y: left(x, y+1) if y % 3 == 0 else up(x, y+1) if y % 3 == 1 else right(x, y+1),
                'down': lambda x, y: right(x, y+1) if y % 3 == 0 else down(x, y+1) if y % 3 == 1 else left(x, y+1),
                'left': lambda x, y: down(x, y+1) if y % 3 == 0 else left(x, y+1) if y % 3 == 1 else up(x, y+1),
                'right': lambda x, y: up(x, y+1) if y % 3 == 0 else right(x, y+1) if y % 3 == 1 else down(x, y+1),
            }

curr_locs = start_locs

while len(curr_locs) > 1:
    new_locs = []
    new_dirs = []
    new_counts = []

    to_be_removed = []
    for l, loc in enumerate(curr_locs):
        n_loc, n_dir, n_count = loc_dict[loc[0]][loc[1]](loc[0], loc[2])

        if n_loc in [x for (x, y, z) in curr_locs]:
            to_be_removed.append(n_loc)
        
        new_locs.append(n_loc)
        new_dirs.append(n_dir)
        new_counts.append(n_count)

    if len(to_be_removed) % 2 == 0:
        new_locs = [x if not x in to_be_removed else None for x in new_locs]

    tmp_counter = Counter(new_locs)
    new_locs = [x if tmp_counter[x] == 1 else None for x in new_locs]

    joined_locs = [(new_locs[i], new_dirs[i], new_counts[i]) for i in range(len(new_locs)) if new_locs[i] != None]

    curr_locs = sorted(joined_locs, key=lambda x: (x[0][1], x[0][0]))

result = curr_locs[0][0]
print(str(result[0]) + ',' + str(result[1]))
