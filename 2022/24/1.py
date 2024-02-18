with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

blizzards = []
max_y, max_x = len(data), len(data[0])

def right(x, y, steps):
    return (x + steps) % (max_x - 2), y

def left(x, y, steps):
    return (x - steps) % (max_x - 2), y

def up(x, y, steps):
    return x, (y - steps) % (max_y - 2)

def down(x, y, steps):
    return x, (y + steps) % (max_y - 2)

for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column == '>':
            blizzards.append((i-1, j-1, right))
        elif column == '<':
            blizzards.append((i-1, j-1, left))
        elif column == '^':
            blizzards.append((i-1, j-1, up))
        elif column == 'v':
            blizzards.append((i-1, j-1, down))

def bfs(blizzards, curr_steps=1):
    steps = curr_steps
    positions = set([start_pos])

    while True:
        next_positions = set()
        blizzard_pos = [func(x, y, steps) for (x, y, func) in blizzards]
        blizzard_pos = [(i+1, j+1) for (i, j) in blizzard_pos]
        for x, y in positions:
            for new_x, new_y in ((x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if (new_x, new_y) == end_pos:
                    return steps
                if 1 <= new_x < max_x - 1 and 1 <= new_y < max_y - 1 and not (new_x, new_y) in blizzard_pos:
                    next_positions.add((new_x, new_y))

        positions = next_positions
        if not positions:
            positions.add(start_pos)
        steps += 1

start_pos = (1, 0)
end_pos = (max_x-2, max_y-1)
nr_steps = bfs(blizzards)

print(nr_steps)
