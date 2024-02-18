value_dict = {}
energized = set()
max_x = 0
max_y = 0
splits = set()

def evaluate(s_loc, s_dir):
    curr_loc = s_loc
    curr_dir = s_dir

    energized = set()

    while True:
        if curr_dir == 'east':
            curr_loc = (curr_loc[0]+1, curr_loc[1])
        elif curr_dir == 'west':
            curr_loc = (curr_loc[0]-1, curr_loc[1])
        elif curr_dir == 'north':
            curr_loc = (curr_loc[0], curr_loc[1]-1)
        elif curr_dir == 'south':
            curr_loc = (curr_loc[0], curr_loc[1]+1)
        
        if curr_loc in value_dict.keys():
            energized.add(curr_loc)
            if (curr_dir, curr_loc) in splits:
                return energized
            elif value_dict[curr_loc] == '|':
                splits.add((curr_dir, curr_loc))
                if curr_dir == 'north' or curr_dir == 'south':
                    energized = energized | evaluate(curr_loc, curr_dir)
                elif curr_dir == 'east' or curr_dir == 'west':
                    eval_one = evaluate(curr_loc, 'north')
                    eval_two = evaluate(curr_loc, 'south')
                    energized = energized | eval_one
                    energized = energized | eval_two
                return energized
            elif value_dict[curr_loc] == '-':
                splits.add((curr_dir, curr_loc))
                if curr_dir == 'east' or curr_dir == 'west':
                    energized = energized | evaluate(curr_loc, curr_dir)
                elif curr_dir == 'north' or curr_dir == 'south':
                    eval_one = evaluate(curr_loc, 'east')
                    eval_two = evaluate(curr_loc, 'west')
                    energized = energized | eval_one
                    energized = energized | eval_two
                return energized
            elif value_dict[curr_loc] == '\\':
                splits.add((curr_dir, curr_loc))
                if curr_dir == 'east':
                    energized = energized | evaluate(curr_loc, 'south')
                elif curr_dir == 'west':
                    energized = energized | evaluate(curr_loc, 'north')
                elif curr_dir == 'north':
                    energized = energized | evaluate(curr_loc, 'west')
                elif curr_dir == 'south':
                    energized = energized | evaluate(curr_loc, 'east')
                return energized
            elif value_dict[curr_loc] == '/':
                splits.add((curr_dir, curr_loc))
                if curr_dir == 'east':
                    energized = energized | evaluate(curr_loc, 'north')
                elif curr_dir == 'west':
                    energized = energized | evaluate(curr_loc, 'south')
                elif curr_dir == 'north':
                    energized = energized | evaluate(curr_loc, 'east')
                elif curr_dir == 'south':
                    energized = energized | evaluate(curr_loc, 'west')
                return energized
        elif curr_loc[0] < 0 or curr_loc[0] >= max_x:
            return energized
        elif curr_loc[1] < 0 or curr_loc[1] >= max_y:
            return energized
        else:
            energized.add(curr_loc)

with open('input.txt') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

max_y = len(rows)
max_x = len(rows[0])

for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column != '.':
            value_dict[(i, j)] = column

s_loc = (-1,0)
s_dir = 'east'

print(len(evaluate(s_loc, s_dir)))
