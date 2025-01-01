from collections import defaultdict
import heapq

with open('input.txt') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

board = {}
special_pos = []
for y, row in enumerate(rows):
    for x, column in enumerate(row):
        if column in ['.', '#']:
            board[(x, y)] = column
        elif column == ' ':
            board[(x, y)] = '#'
        else:
            board[(x, y)] = column
            special_pos.append((x, y))

pos_dict = defaultdict(list)
visited = set()
for p in special_pos:
    if p in visited:
        continue

    ns = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nodes = [(p[0]+n[0], p[1]+n[1]) for n in ns]
    other = [n for n in nodes if board.get(n, 'a').isupper()][0]
    diff_x = other[0]-p[0]
    diff_y = other[1]-p[1]

    name = board[p] + board[other]
    new_val = None
    match (diff_x, diff_y):
        case (1, 0):
            if board.get((other[0]+1, other[1]), None) == '.':
                new_val = (other[0]+1, other[1])
            else:
                new_val = (p[0]-1, p[1])
        case (0, 1):
            if board.get((other[0], other[1]+1), None) == '.':
                new_val = (other[0], other[1]+1)
            else:
                new_val = (p[0], p[1]-1)
        case _:
            assert False

    board[new_val] = name
    pos_dict[name].append(new_val)

    board[p] = '#'
    board[other] = '#'
    
    visited.add(p)
    visited.add(other)

start_node = pos_dict['AA'][0]

queue = [(start_node, 0)]
visited = {start_node}
while queue:
    node, weight = heapq.heappop(queue)

    ns = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ns = [(node[0]+n[0], node[1]+n[1]) for n in ns]
    ns = [n for n in ns if not n in visited]
    ns = [n for n in ns if board[n] != '#']

    for n in ns:
        visited.add(node)

        if board[n] == 'ZZ':
            print(weight+1)
            break

        if board[n] == '.':
            heapq.heappush(queue, (n, weight+1))
        else:
            teleport = [x for x in pos_dict[board[n]] if not x == n][0]
            heapq.heappush(queue, (teleport, weight+2))

    queue = sorted(queue, key=lambda x: x[1])
