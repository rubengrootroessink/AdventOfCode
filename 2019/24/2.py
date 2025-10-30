from collections import defaultdict

def neighbours(depth, i, j):
    cns = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    cns = [(depth, i, j) for (i, j) in cns if i in range(5) and j in range(5) and not (i, j) == (2, 2)]

    if i == 0:
        cns.append((depth-1, 1, 2))
    elif i == 4:
        cns.append((depth-1, 3, 2))
    
    if j == 0:
        cns.append((depth-1, 2, 1))
    elif j == 4:
        cns.append((depth-1, 2, 3))

    if (i, j) == (1, 2):
        for n in range(5):
            cns.append((depth+1, 0, n))
    elif (i, j) == (3, 2):
        for n in range(5):
            cns.append((depth+1, 4, n))
    elif (i, j) == (2, 1):
        for n in range(5):
            cns.append((depth+1, n, 0))
    elif (i, j) == (2, 3):
        for n in range(5):
            cns.append((depth+1, n, 4))

    return cns

def minute(board):
    new_board = defaultdict(int)

    potential_changes = set()
    for (depth, i, j) in sorted(list(board.keys())):
        potential_changes.add((depth, i, j))
        for n in neighbours(depth, i, j):
            potential_changes.add(n)

    for (depth, i, j) in potential_changes:
        nns = len([board[(s, k, l)] for (s, k, l) in neighbours(depth, i, j) if board[(s, k, l)] == 1])
        if board[(depth, i, j)] == 1 and nns == 1: # Bug survives
            new_board[(depth, i, j)] = 1
        elif board[(depth, i, j)] == 0 and nns in [1, 2]: # Empty space infested
            new_board[(depth, i, j)] = 1

    return new_board

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

board = defaultdict(int)
depth = 0
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column == '#':
            board[(0, i, j)] = 1

for i in range(0, 200):
    board = minute(board)
print(len(board))
