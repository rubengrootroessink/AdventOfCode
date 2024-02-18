draws = []
boards = []
with open('input.txt', 'r') as file:
    data = file.read().rsplit('\n', 1)[0].split('\n\n')
    draws = [int(x) for x in data[0].split(',')]
    boards = [[int(x) for x in ' '.join(board.split('\n')).split()] for board in data[1:]]

def bingo(board, n=5):
    converted_board = [board[i:i+n] for i in range(0, len(board), n)]
    transposed = [list(sublist) for sublist in list(zip(*converted_board))]
    return any([all(element == row[0] for element in row) for row in converted_board]) or any([all(element == row[0] for element in row) for row in transposed])

def value(board):
    return sum([x for x in board if not x is None])

def run(draws, boards):
    winning_boards = set()
    curr_boards = boards
    for draw in draws:
        new_boards = []
        for i, board in enumerate(curr_boards):
            new_board = [x if x != draw else None for x in board]
            if bingo(new_board) and len(winning_boards) == len(boards) - 1 and not i in winning_boards:
                return draw, value(new_board)
            elif bingo(new_board):
                winning_boards.add(i)
                new_boards.append(new_board)
            else:
                new_boards.append(new_board)
        curr_boards = new_boards

draw, board = run(draws, boards)
print(draw * board)
