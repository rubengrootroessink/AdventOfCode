board = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        board.append(data)
        
row_length = len(board[0])
target = len(board) - 1

count = 0
x, y = 0, 0

while not y == target:
    x = (x + 3) % row_length
    y += 1
    if board[y][x] == '#':
        count += 1
        
print(count)
