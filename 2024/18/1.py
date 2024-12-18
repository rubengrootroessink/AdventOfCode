from collections import defaultdict
import heapq

with open('input.txt') as f:
    corrupted = [tuple([int(y) for y in x.strip().split(',')]) for x in f.readlines()]

corrupted = set(corrupted[:1024])

memory = set()

size = 70
for y in range(0, size+1):
    for x in range(0, size+1):
        if not (x, y) in corrupted:
            memory.add((x, y))

ntfs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

s = (0, 0)
e = (size, size)
visited = {s}

queue = [(s, 0)]
while queue:
    node, weight = heapq.heappop(queue)

    if node == e:
        print(weight)
        break

    ns = [(node[0] + n[0], node[1] + n[1]) for n in ntfs]
    ns = [n for n in ns if n in memory and not n in visited]

    for n in ns:
        heapq.heappush(queue, (n, weight+1))
        visited.add(n)

    queue = sorted(queue, key=lambda x: x[1])
