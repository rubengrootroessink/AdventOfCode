with open('input.txt') as f:
    board = [list(x.split('\n')[0]) for x in f.readlines()]
    board = [['.'] * len(board[0])] + board
    board = board + [['.'] * len(board[0])]
    board = [['.'] + x + ['.'] for x in board]

s = (None, None)
for y, row in enumerate(board):
    for x, column in enumerate(row):
        if column == 'S':
            s = (x, y)

evaluated = {}
to_evaluate = [(s, 0)]

while len(to_evaluate) > 0:
    curr_tile, curr_path_length = to_evaluate[0]

    if evaluated == {} and len(to_evaluate) == 1: # Starting node
        adjacent_tiles = [
            (curr_tile[0], curr_tile[1]-1),
            (curr_tile[0]+1, curr_tile[1]),
            (curr_tile[0], curr_tile[1]+1),
            (curr_tile[0]-1, curr_tile[1])
        ]

        new_tiles = []
        for i, item in enumerate(adjacent_tiles):
            tile_val = board[item[1]][item[0]]
            if i == 0:
                if tile_val in ['|', 'F', '7']:
                    new_tiles.append(item)
            elif i == 1:
                if tile_val in ['-', 'J', '7']:
                    new_tiles.append(item)
            elif i == 2:
                if tile_val in ['|', 'L', 'J']:
                    new_tiles.append(item)
            elif i == 3:
                if tile_val in ['-', 'L', 'F']:
                    new_tiles.append(item)

        new_tiles = [(x, curr_path_length+1) for x in new_tiles if not x in evaluated.keys()]
        to_evaluate = to_evaluate[1:] + new_tiles
        evaluated[curr_tile] = curr_path_length
    
    else:
        tile_val = board[curr_tile[1]][curr_tile[0]]
        new_tiles = None
        match tile_val:
            case '|':
                new_tiles = [(curr_tile[0], curr_tile[1]-1), (curr_tile[0], curr_tile[1]+1)]
            case '-':
                new_tiles = [(curr_tile[0]-1, curr_tile[1]), (curr_tile[0]+1, curr_tile[1])]
            case 'L':
                new_tiles = [(curr_tile[0], curr_tile[1]-1), (curr_tile[0]+1, curr_tile[1])]
            case 'J':
                new_tiles = [(curr_tile[0], curr_tile[1]-1), (curr_tile[0]-1, curr_tile[1])]
            case '7':
                new_tiles = [(curr_tile[0], curr_tile[1]+1), (curr_tile[0]-1, curr_tile[1])]
            case 'F':
                new_tiles = [(curr_tile[0], curr_tile[1]+1), (curr_tile[0]+1, curr_tile[1])]

        new_tiles = [x for x in new_tiles if not x in evaluated.keys()]
        if len(new_tiles) == 1:
            new_tile = new_tiles[0]
            to_evaluate = to_evaluate[1:] + [(new_tile, curr_path_length+1)]
            evaluated[curr_tile] = curr_path_length
        else:
            to_evaluate = []
            evaluated[curr_tile] = curr_path_length

print(max(evaluated.values()))
