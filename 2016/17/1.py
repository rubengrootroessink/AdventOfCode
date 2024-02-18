import heapq
import hashlib

with open('input.txt') as f:
    passcode = f.read().strip()

start_pos = (0, 0)
shortest_path = None

heap = [(start_pos, '')]
while heap:
    pos, path = heapq.heappop(heap)

    if pos == (3, 3):
        if shortest_path == None or len(path) < len(shortest_path):
            shortest_path = path

    md5 = hashlib.md5((passcode + path).encode()).hexdigest()[0:4]
    
    neighbours = [
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1),
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
    ]

    directions = ['U', 'D', 'L', 'R']

    open_neighbours = [(n, directions[i]) for i, n in enumerate(neighbours) if md5[i] in ['b', 'c', 'd', 'e', 'f']]
    open_neighbours = [(n, d) for (n, d) in open_neighbours if n[0] in range(0, 4) and n[1] in range(0, 4)]

    for (n, d) in open_neighbours:
        heapq.heappush(heap, (n, path + d))

    if shortest_path != None:
        heap = [x for x in heap if len(x[1]) <= len(shortest_path)]

    heap = list(sorted(heap, key=lambda x: len(x[1])))

print(shortest_path)
