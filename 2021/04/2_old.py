draws = []
boards = []
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

draws = [int(x) for x in data[0].split(',')]
raw_boards = [x.split('\n') for x in data[1:]]

boards = []
for board in raw_boards:
    new_board = []
    print(board)
    for row in board:
        new_row = row.split()
        print(new_row)
        new_row = [int(x) for x in new_row]
        if new_row != []:
            new_board.append(new_row)        

    boards.append(new_board)

print(boards)

def check_row_or_column(board):
    for row in board:
        if all(element == row[0] for element in row):
            return True

    transposed = list(zip(*board))
    transposed = [list(sublist) for sublist in transposed]
    for column in transposed:
        if all(element == column[0] for element in column):
            return True

def cal_vals(board):
    total_val = 0
    for row in board:
        for column in row:
            if not column is None:
                total_val += column
    return total_val

found = False
val = 0
last_draw = None
winning_boards = []
last = None
for draw in draws:
    print('DRAW', draw)

    if found:
        break;

    last_draw = draw

    for i, board in enumerate(boards):
        #if i in winning_boards:
        #    break;
        for j, row in enumerate(board):
            for k, item in enumerate(row):
                if item == draw:
                    boards[i][j][k] = None

        print(len(winning_boards), len(boards) - 1)
        if check_row_or_column(board) and not i in winning_boards:
            winning_boards.append(i)
            last = i

        if check_row_or_column(board) and len(winning_boards) == len(boards):
            found = True  
            break;

    print(winning_boards)
    print('\n'.join([str(board) for board in boards]))

val = cal_vals(boards[i]) 
print(i)
print(val * last_draw)
