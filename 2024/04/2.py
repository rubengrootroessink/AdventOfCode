from collections import defaultdict

board = defaultdict(str)
a_pos = []

def construct(board, x, y):
    star_locs = [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
    star = ''.join([board[(x+i,y+j)] for (i, j) in star_locs])
    if len(star) == 5 and star.count('M') == 2 and star.count('S') == 2 and star[1] != star[3]:
        return 1
    return 0

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

for j, row in enumerate(data):
    for i, column in enumerate(row):
        board[(i,j)] = column
        if column == 'A':
            a_pos.append((i,j))

res_count = 0
for val in a_pos:
    res_count += construct(board, val[0], val[1])

print(res_count)
