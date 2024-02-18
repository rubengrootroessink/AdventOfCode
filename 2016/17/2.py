import heapq
import hashlib

with open('input.txt') as f:
    passcode = f.read().strip()

start_pos = (0, 0)
longest_path = 0

heap = [(start_pos, '')]
while heap:
    pos, path = heapq.heappop(heap)

    if pos == (3, 3):
        if len(path) > longest_path:
            longest_path = len(path)
    else:
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

        heap = list(sorted(heap, key=lambda x: -len(x[1])))

print(longest_path)
