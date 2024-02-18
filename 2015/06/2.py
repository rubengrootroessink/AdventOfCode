board = []

for i in range(0, 1000):
    row = []
    for j in range(0, 1000):
        row.append(0)
    board.append(row)
    
with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split(' ')
        command = 'toggle on'
        min_x, min_y = 0, 0
        max_x, max_y = 0, 0
        if data[0] == 'turn':
            command = data[0] + ' ' + data[1]
            min_x, min_y = [int(x) for x in data[2].split(',')]
            max_x, max_y = [int(x) + 1 for x in data[4].split(',')]
        else:
            command = 'toggle'
            min_x, min_y = [int(x) for x in data[1].split(',')]
            max_x, max_y = [int(x) + 1 for x in data[3].split(',')]
            
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if command == 'toggle':
                    board[i][j] += 2
                elif command == 'turn on':
                    board[i][j] += 1
                elif command == 'turn off':
                    if board[i][j] > 0:
                        board[i][j] -= 1

print(board[i])

count = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        count += board[i][j]

print(count)
