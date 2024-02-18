import heapq

value_dict = {}

max_x = 0
max_y = 0
cave = []

alphabet = 'SabcdefghijklmnopqrstuvwxyzE'

with open('input.txt') as f:
    cave = [list(line.strip()) for line in f.readlines()]
    max_x = len(cave[0])
    max_y = len(cave)

def in_cave(y, x):
    return 0 <= y < max_y and 0 <= x < max_x

def check_val(val, y, x, cave):
    curr_index = alphabet.index(val)
    next_index = alphabet.index(cave[y][x])

    if next_index > curr_index and next_index - curr_index > 1:
        return False
    elif next_index > curr_index and next_index - curr_index == 1:
        return True
    elif next_index > curr_index:
        assert False
    elif next_index < curr_index or next_index == curr_index:
        return True

def dijkstra(cave):
    start_node, end_node = (0,0), (0,0)
    for y, row in enumerate(cave):
        for x, column in enumerate(row):
            if column == 'S':
                start_node = (y, x)
            elif column == 'E':
                end_node = (y, x)

    heap, visited = [(0,) + start_node], {start_node}

    while heap:
        
        steps, y, x = heapq.heappop(heap)
        
        if (y, x) == end_node: return steps

        neighbours = [
            (y-1, x), (y+1, x),
            (y, x-1), (y, x+1),
        ]

        for dy, dx in neighbours:
            if (dy, dx) in visited or not in_cave(dy, dx) or not check_val(cave[y][x], dy, dx, cave):
                continue
            heapq.heappush(heap, (steps + 1, dy, dx))
            visited.add((dy, dx))

print(dijkstra(cave))
