import math

def check_slope(board, target, row_length, num_x, num_y):
    x, y = 0, 0
    count = 0
    while not y == target:
        x = (x + num_x) % row_length
        y += num_y
        if board[y][x] == '#':
            count += 1
    return count

board = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        board.append(data)
        
row_length = len(board[0])
target = len(board) - 1

result = []
for i in range(1, 9, 2):
    result.append(check_slope(board, target, row_length, i, 1))
result.append(check_slope(board, target, row_length, 1, 2))

print(math.prod(result))
