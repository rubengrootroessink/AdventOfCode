def check_tile(board, x, y):
    min_x = max(x-1, 0)
    max_x = min(x+2, len(board))
    
    min_y = max(y-1, 0)
    max_y = min(y+2, len(board[0]))
    
    count = 0
    empty_count = 0
    occupied_count = 0

    if board == '.':
        return False

    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            if not (i == x and j == y):

                if board[i][j] == '.':
                   step_x = i - x
                   step_y = j - y
                   
                   new_x = i + step_x
                   new_y = j + step_y

                   seat = False
                   while not seat and new_x in range(0, len(board)) and new_y in range(0, len(board[0])):
                       if board[new_x][new_y] != '.':
                           seat = True
                           if board[new_x][new_y] == 'L':
                               empty_count += 1
                           else:
                               occupied_count += 1
                           
                           count += 1
                       elif board[new_x][new_y] == '.':
                           new_x += step_x
                           new_y += step_y
                
                elif board[i][j] == 'L':
                    empty_count += 1
                    count += 1
                else:
                    occupied_count += 1
                    count += 1

    if empty_count == count and board[x][y] == 'L':
        return True
    elif occupied_count >= 5 and board[x][y] == '#':
        return True
    return False

def change(board, count):
    new_board = []
    for x in range(len(board)):
        row = []
        for y in range(len(board[0])):
            if check_tile(board, x, y):
                if board[x][y] == 'L':
                    row.append('#')
                else:
                    row.append('L')
            else:
                 row.append(board[x][y])
        new_board.append(row)
        
    new_board_str = ''.join(ele for sub in new_board for ele in sub)
    old_board_str = ''.join(ele for sub in board for ele in sub)
    
    if new_board_str == old_board_str:
        return True, board
    else:
        return False, new_board
    
def count_occupied(board):
    count = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == '#':
                count += 1
    return count

with open('input.txt', 'r') as file:
    board = []
    for i, line in enumerate(file.readlines()):
        row = []
        data = line.split("\n")[0]
        for seat in data:
            row.append(seat)
            
        board.append(row)
    found = False
    count = 0
    while not found:
        result = change(board, count)
        count += 1
        if result[0]:
            found = True
        board = result[1]
    print(count_occupied(board))
