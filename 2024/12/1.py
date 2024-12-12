from collections import defaultdict
import heapq
import copy

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
    perimeter = len([1 for n in nbs if not board[(x+n[0], y+n[1])] == val])
    perimeter_dict[key] = perimeter

resolved = set()
price = 0

for i, key in enumerate(keys):
    if key in resolved:
        pass
    else:
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
        
        price += len(block) * sum([perimeter_dict[n] for n in block])

print(price)
