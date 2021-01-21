import copy

def check_valid(x, y, i, j, length):
    return i >= 0 and i < length and j >= 0 and j < length and not (x == i and y == j)

def count_neighbours(board, x, y, length):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if check_valid(x, y, i, j, length):
                if board[i][j] == '#':
                    count += 1
    return count
    
def step(board, length):
    new_board = copy.deepcopy(board)
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            count = count_neighbours(board, i, j, length)
            isCorner = (i == 0 and j == 0) or (i == 0 and j == length - 1) or (i == length - 1 and j == 0) or (i == length - 1 and j == length - 1)
            if column == '#' and not count in [2, 3] and not isCorner:
                new_board[i][j] = '.'
            elif column == '.' and count == 3 and not isCorner:
                new_board[i][j] = '#'
    return new_board

with open('input.txt', 'r') as f:
    board = []
    for line in f.readlines():
        board.append(list(line.split('\n')[0]))

    length = len(board)
    board[0][0] = '#'
    board[0][length-1] = '#'
    board[length-1][0] = '#'
    board[length-1][length-1] = '#'

    nr_runs = 100
    for i in range(0, nr_runs):
        board = step(board, length)

    print(sum([sum([1 if y == '#' else 0 for y in x]) for x in board]))
