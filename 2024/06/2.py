import copy
from multiprocessing import Process, Manager
from collections import defaultdict

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def run(start_pos, board):
    x, y = start_pos
    dir_index = 0
    cycle = set()

    while True:
        fwd = directions[dir_index]
        n_x, n_y = x + fwd[0], y + fwd[1]

        if board[(n_x, n_y)] == '':
            return True
        elif board[(n_x, n_y)] == '#':
            dir_index = (dir_index + 1) % 4
            if ((x, y), dir_index) in cycle:
                return False
            cycle.add(((x, y), dir_index))
        else:
            x, y = n_x, n_y

def con_run(procnum, candidate, board, return_dict):
    n_board = copy.deepcopy(board)
    n_board[candidate] = '#'
    return_dict[procnum] = run(start_pos, n_board)

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

start_pos = None
board = defaultdict(str)
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        board[(i,j)] = column
        if column == '^':
            start_pos = (i,j)

x, y = start_pos
dir_index = 0
locs = []
while board[(x,y)] != '':
    fwd = directions[dir_index]
    n_x, n_y = x + fwd[0], y + fwd[1]
    if board[(n_x,n_y)] == '#':
        dir_index = (dir_index + 1) % 4
    else:
        x, y = n_x, n_y
        locs.append((x, y))

candidates = list(set(locs))

manager = Manager()
batch_size = 20

result = 0
for i in range(0, len(candidates), batch_size):
    return_dict = manager.dict()
    processes = [Process(target=con_run, args=(j, candidates[j], board, return_dict)) for j in range(i, min(i+batch_size, len(candidates)))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    
    result += len([x for x in return_dict.values() if not x])

print(result)
