from collections import defaultdict
import sys
import heapq

with open('input.txt') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

max_x = len(rows[0])-3
max_y = len(rows)-3

inner_x_min, inner_x_max = sys.maxsize, 0
inner_y_min, inner_y_max = sys.maxsize, 0

for y, row in enumerate(rows):
    for x, column in enumerate(row):
        if not column in ['#', '.', ' ']:
            if not x in range(0, 2) and not x in range(max_x+1, max_x+3):
                if not y in range(0, 2) and not y in range(max_y+1, max_y+3):
                    inner_x_min = min(x, inner_x_min)
                    inner_x_max = max(x, inner_x_max)
                    inner_y_min = min(y, inner_y_min)
                    inner_y_max = max(y, inner_y_max)

inner_x_min -= 1
inner_x_max += 1
inner_y_min -= 1
inner_y_max += 1

special_pos = defaultdict(dict)
board = {}
for y, row in enumerate(rows):
    for x, column in enumerate(row):
        if y == 2 and column == '.':
            name = rows[0][x] + rows[1][x]
            board[(x, y)] = name
            special_pos[name]['O'] = (x, y)
        elif y == max_y and column == '.':
            name = rows[-2][x] + rows[-1][x]
            board[(x, y)] = name
            special_pos[name]['O'] = (x, y)
        elif x == 2 and column == '.':
            name = rows[y][0] + rows[y][1]
            board[(x, y)] = name
            special_pos[name]['O'] = (x, y)
        elif x == max_x and column == '.':
            name = rows[y][-2] + rows[y][-1]
            board[(x, y)] = name
            special_pos[name]['O'] = (x, y)
        elif x == inner_x_min and column == '.' and y in range(inner_y_min, inner_y_max):
            name = rows[y][x+1] + rows[y][x+2]
            board[(x, y)] = name
            special_pos[name]['I'] = (x, y)
        elif x == inner_x_max and column == '.' and y in range(inner_y_min, inner_y_max):
            name = rows[y][x-2] + rows[y][x-1]
            board[(x, y)] = name
            special_pos[name]['I'] = (x, y)
        elif y == inner_y_min and column == '.' and x in range(inner_x_min, inner_x_max):
            name = rows[y+1][x] + rows[y+2][x]
            board[(x, y)] = name
            special_pos[name]['I'] = (x, y)
        elif y == inner_y_max and column == '.' and x in range(inner_x_min, inner_x_max):
            name = rows[y-2][x] + rows[y-1][x]
            board[(x, y)] = name
            special_pos[name]['I'] = (x, y)
        elif column == '.':
            board[(x, y)] = '.'
        else:
            board[(x, y)] = '#'

graph = defaultdict(dict)

neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for name, loc_dict in special_pos.items():
    for direction, loc in loc_dict.items():
        
        queue = [(loc, 0)]
        visited = {loc}
        while queue:
            node, steps = heapq.heappop(queue)

            if node != loc and board[node] in special_pos.keys():
                val = special_pos[board[node]]
                if val.get('I', None) == node:
                    graph[(name, direction)][(board[node], 'I')] = steps
                else:
                    graph[(name, direction)][(board[node], 'O')] = steps
                    
            ns = [(node[0]+n[0], node[1]+n[1]) for n in neighbours]
            ns = [n for n in ns if not n in visited]
            ns = [n for n in ns if board[n] != '#']

            for n in ns:
                visited.add(n)
                heapq.heappush(queue, (n, steps+1))

queue = [('AA', 'O', 0, 0)]
visited = {('AA', 'O', 0)}
found = False
while queue and not found:
    name, side, steps, depth = heapq.heappop(queue)

    if name == 'ZZ':
        continue
    if name == 'AA' and depth != 0:
        continue

    options = [(k, v) for k, v in graph[(name, side)].items() if not k in visited]
    
    for k, v in options:
        new_depth = depth-1 if k[1] == 'O' else depth+1
    
        if k[0] == 'ZZ' and depth == 0:
            print(steps + v)
            found = True
            break

        if new_depth >= 0:
            heapq.heappush(queue, (k[0], 'I' if k[1] == 'O' else 'O', steps+v+1, new_depth))
            visited.add((k[0], k[1], new_depth))

    queue = sorted(queue, key=lambda x: (x[3], x[2]))
