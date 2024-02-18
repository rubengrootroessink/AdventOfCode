import re

with open('input.txt') as f:
    board = [x.split('\n')[0] for x in f.readlines()]

g = re.compile('\*')
p = re.compile('\d+')

parts = []

gears = []
for i, row in enumerate(board):
    for match in g.finditer(row):
        j, _ = match.span()
        gears.append((i, j))

result = 0
for gear in gears:
    matching_parts = []

    gear_row, gear_column = gear

    gear_neighbours = [(gear_row-1, gear_column-x) for x in [-1, 0, 1]]
    gear_neighbours += [(gear_row, gear_column-x) for x in [-1, 0, 1]]
    gear_neighbours += [(gear_row+1, gear_column-x) for x in [-1, 0, 1]]

    rows = list(map(lambda z: [y for y in range(0, len(board))][z], [gear[0]+x for x in [-1, 0, 1] if gear[0]+x in range(0, len(board))]))
    for index in rows:
        for match in p.finditer(board[index]):
            part_id = int(match.group())
            part_start, part_end = match.span()

            part_indices = [(index, x) for x in range(part_start, part_end)]
            for p_i in part_indices:
                if p_i in gear_neighbours:
                    matching_parts.append(part_id)
                    break

    assert len(matching_parts) <= 2
    if len(matching_parts) == 2:
        result += matching_parts[0] * matching_parts[1]

print(result)
