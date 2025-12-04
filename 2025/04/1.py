import copy

def clean(curr_board):
    new_board = copy.deepcopy(curr_board)

    for k, v in curr_board.items():
        if v == 1:
            (i, j) = k
            i_range = range(i-1, i+2)
            j_range = range(j-1, j+2)
            count = 0
            for l in i_range:
                for m in j_range:
                    if (l, m) in curr_board.keys() and (l, m) != (i, j):
                        count += 1

            if count < 4:
                del new_board[(i, j)]
    
    return new_board

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

board = {}
start_size = 0
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column == '@':
            board[(i, j)] = 1
            start_size += 1

print(start_size - len(clean(board)))
