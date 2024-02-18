import heapq

# Read input
with open('input.txt') as f:
    board = [list(x.split('\n')[0]) for x in f.readlines()]
    board = [['O'] * (len(board[0])+2)] + [['O'] + x + ['O'] for x in board] + [['O'] * (len(board[0])+2)]

s_node = (None, None)
for y, row in enumerate(board):
    for x, column in enumerate(row):
        if column == 'S':
            s_node = (x, y)

# Find all columns that are part of the loop
in_path = set()
to_evaluate = [s_node]
while to_evaluate:
    curr = heapq.heappop(to_evaluate)
    curr_val = board[curr[1]][curr[0]]
    
    in_path.add(curr)

    if curr == s_node: # Starting node
        neighbours = [
            (curr[0], curr[1]-1),
            (curr[0]+1, curr[1]),
            (curr[0], curr[1]+1),
            (curr[0]-1, curr[1])
        ]

        match_vals = [
            ['|', 'F', '7'], # North connection
            ['-', 'J', '7'], # East connection
            ['|', 'L', 'J'], # South connection
            ['-', 'L', 'F'], # West connection
        ]

        neighbours = [item for i, item in enumerate(neighbours) if board[item[1]][item[0]] in match_vals[i] and not item in in_path]

    else:
        neighbour_dict = [
            [(curr[0], curr[1]-1), (curr[0], curr[1]+1)], # |
            [(curr[0]-1, curr[1]), (curr[0]+1, curr[1])], # -
            [(curr[0], curr[1]-1), (curr[0]+1, curr[1])], # L
            [(curr[0], curr[1]-1), (curr[0]-1, curr[1])], # J
            [(curr[0], curr[1]+1), (curr[0]-1, curr[1])], # 7
            [(curr[0], curr[1]+1), (curr[0]+1, curr[1])]  # F
        ]

        neighbours = [x for x in neighbour_dict[['|', '-', 'L', 'J', '7', 'F'].index(curr_val)] if not x in in_path]

    for neighbour in neighbours:
        heapq.heappush(to_evaluate, neighbour)

# Create a new board entirely consisting of only '.' and the loop (to remove all non-useful values)
clean_board = [['.' for x in y] for y in board]
for item in in_path:
    clean_board[item[1]][item[0]] = board[item[1]][item[0]]
board = [x[1:-1] for x in clean_board[1:-1]]

# Enlarge board to accomodate flood filling between pipes
enlarged_board = []
for y, row in enumerate(board):
    row_1, row_2, row_3 = [], [], []
    for x, column in enumerate(row):
        if column == '.':
            row_1 = row_1 + ['.', '.', '.']
            row_2 = row_2 + ['.', '.', '.']
            row_3 = row_3 + ['.', '.', '.']
        elif column == 'F':
            row_1 = row_1 + ['.', '.', '.']
            row_2 = row_2 + ['.', 'F', '-']
            row_3 = row_3 + ['.', '|', '.']
        elif column == 'J':
            row_1 = row_1 + ['.', '|', '.']
            row_2 = row_2 + ['-', 'J', '.']
            row_3 = row_3 + ['.', '.', '.']
        elif column == 'L':
            row_1 = row_1 + ['.', '|', '.']
            row_2 = row_2 + ['.', 'L', '-']
            row_3 = row_3 + ['.', '.', '.']
        elif column == '7':
            row_1 = row_1 + ['.', '.', '.']
            row_2 = row_2 + ['-', '7', '.']
            row_3 = row_3 + ['.', '|', '.']
        elif column == '|':
            row_1 = row_1 + ['.', '|', '.']
            row_2 = row_2 + ['.', '|', '.']
            row_3 = row_3 + ['.', '|', '.']
        elif column == '-':
            row_1 = row_1 + ['.', '.', '.']
            row_2 = row_2 + ['-', '-', '-']
            row_3 = row_3 + ['.', '.', '.']
        elif column == 'S':
            r_1 = ['.', '.', '.']
            r_2 = ['.', 'S', '.']
            r_3 = ['.', '.', '.']
            
            if board[y][x+1] in ['J', '-', '7']:
                r_2[2] = '-'
            if board[y][x-1] in ['L', '-', 'F']:
                r_2[0] = '-'
            if board[y+1][x] in ['L', '|', 'J']:
                r_3[1] = '|'
            if board[y-1][x] in ['7', '|', 'F']:
                r_1[1] = '|'

            row_1 = row_1 + r_1
            row_2 = row_2 + r_2
            row_3 = row_3 + r_3

    enlarged_board.append(row_1)
    enlarged_board.append(row_2)
    enlarged_board.append(row_3)

# Add a row of 'O's around the enlarged board to enable flood filling
enlarged_new_board = [['O'] * (len(enlarged_board[0])+2)] + [['O'] + x + ['O'] for x in enlarged_board] + [['O'] * (len(enlarged_board[0])+2)]

# Start of the floodfill algorithm (it currently assumes the value at (1,1) is always '.'
# This was the case for all of my inputs
s = (1,1) # TODO, make generic
enlarged_board = enlarged_new_board

heap = [s]
enlarged_board[s[1]][s[0]] = 'O'

while heap:
    x, y = heapq.heappop(heap)

    neighbours = [
        (x+1, y, enlarged_board[y][x+1]),
        (x-1, y, enlarged_board[y][x-1]),
        (x, y-1, enlarged_board[y-1][x]),
        (x, y+1, enlarged_board[y+1][x])
    ]
    
    neighbours = [(x, y) for x, y, z in neighbours if z == '.']

    for neighbour in neighbours:
        enlarged_board[neighbour[1]][neighbour[0]] = 'O'
        heapq.heappush(heap, neighbour)

unenlarged_board = [x[1:-1] for x in enlarged_board[1:-1]]

splitted_rows = [unenlarged_board[i:i+3] for i in range(0, len(unenlarged_board), 3)]
tmp_board = []
for line in splitted_rows:
    i = 0
    tmp_row = []
    while i < len(line[0]):
        mid_char = line[1][i:i+3][1]
        tmp_row.append(mid_char) 
        i += 3
    tmp_board.append(tmp_row)

print(sum([sum([1 for x in y if x == '.']) for y in tmp_board]))
