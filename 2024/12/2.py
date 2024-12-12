from collections import defaultdict
import heapq

with open('input.txt') as f:
    data = [list(x.strip()) for x in f.readlines()]

ordered_board = defaultdict(list)
board = defaultdict(str)
for j, row in enumerate(data):
    for i, column in enumerate(row):
        board[(i, j)] = column
        ordered_board[column].append((i, j))

nbs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

perimeter_dict = defaultdict(int)
keys = list(board.keys())
for key in keys:
    x, y = key
    val = board[(x, y)]

    perimeter = []
    for n in nbs:
        nb = (x+n[0], y+n[1])
        if board[nb] != val:
            perimeter.append((x + (n[0] / 4), y + (n[1] / 4)))
    perimeter_dict[key] = perimeter

resolved = set()
price = 0

for i, key in enumerate(keys):
    if key in resolved:
        continue
    
    x, y = key
    value = board[key]
    potentials = {o: value for o in ordered_board[value]}

    block = {key}
    visited = {key}

    neighbours = [(x+n[0], y+n[1]) for n in nbs]
    neighbours = [n for n in neighbours if n in potentials and board[n] == value]

    block = {key}
    while neighbours:    
        ev = heapq.heappop(neighbours)
        block.add(ev)
        visited.add(ev)

        nn = [(ev[0]+n[0], ev[1]+n[1]) for n in nbs]
        nn = [n for n in nn if (n in potentials and board[n] == value) and not n in visited]

        for n in nn:
            heapq.heappush(neighbours, n)

        neighbours = list(set(neighbours))

    for item in block:
        resolved.add(item)

    count = 0

    perimeter = set()
    for item in block:
        sides = perimeter_dict[item]
        for side in sides:
            perimeter.add(side)

    sides_visited = set()
    for side in perimeter:
        
        if side in sides_visited:
            continue
        sides_visited.add(side)

        s_x, s_y = side
        
        if float(int(s_x)) == s_x:
            for c in [-1.0, 1.0]:
                new_x = s_x+c
                while (new_x, s_y) in perimeter:
                    sides_visited.add((new_x, s_y))
                    new_x = new_x+c
        elif float(int(s_y)) == s_y:
            for c in [-1.0, 1.0]:
                new_y = s_y+c
                while (s_x, new_y) in perimeter:
                    sides_visited.add((s_x, new_y))
                    new_y = new_y+c
        count += 1

    price += len(block) * count

print(price)
