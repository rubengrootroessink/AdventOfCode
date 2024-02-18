import heapq

value_dict = {}
max_x = 0
max_y = 0
cave = []
with open('input.txt') as f:
    cave = [list(map(int, line.strip())) for line in f.readlines()]
    max_x = len(cave[0])
    max_y = len(cave)

def in_cave(y, x, cave_size):
    return 0 <= y < max_y*cave_size and 0 <= x < max_x*cave_size

def risk_level(cave, y, x):
    risk_level = cave[y%max_y][x%max_x] + x//max_y + y//max_x
    return risk_level % 9 or risk_level

def dijkstra(cave, cave_size=1):
    start_node, end_node = (0,0), (max_y*cave_size-1,max_x*cave_size-1)
    
    heap, visited = [(0,) + start_node], {start_node}

    while heap:
        risk, y, x = heapq.heappop(heap)
        if (y, x) == end_node: return risk

        neighbours = [
            (y-1, x), (y+1, x),
            (y, x-1), (y, x+1),
        ]

        for dy, dx in neighbours:
            if (dy, dx) in visited or not in_cave(dy, dx, cave_size):
                continue
            r = risk_level(cave, dy, dx)
            heapq.heappush(heap, (risk+r, dy, dx))
            visited.add((dy, dx))

print(dijkstra(cave, cave_size=1))

# With extensive help from: https://github.com/piyx/AdventOfCode2021/blob/main/2021/day15_chiton.py
