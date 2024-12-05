from collections import defaultdict

board = defaultdict(str)
x_pos = []

def construct(board, x, y):
    sub_strs = []
    for i in range(-1, 2):
        for j in range(-1,2):
            sub_strs.append(''.join([board[(x+i*k,y+j*k)] for k in range(0,4)]))
    return len([k for k in sub_strs if k == 'XMAS'])

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

for j, row in enumerate(data):
    for i, column in enumerate(row):
        board[(i,j)] = column
        if column == 'X':
            x_pos.append((i,j))

res_count = 0
for val in x_pos:
    res_count += construct(board, val[0], val[1])

print(res_count)
