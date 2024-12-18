from collections import defaultdict
import heapq

def eval(size, memory):
    ntfs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    s = (size, size)
    e = (0, 0)
    
    visited = {s}
    
    queue = [s]
    
    while queue:
        node = heapq.heappop(queue)

        ns = [(node[0] + n[0], node[1] + n[1]) for n in ntfs]
        ns = [n for n in ns if n in memory and not n in visited]

        for n in ns:
            heapq.heappush(queue, n)
            visited.add(n)

    if e in visited:
        return False
    else:
        return True

with open('input.txt') as f:
    corrupted = [tuple([int(y) for y in x.strip().split(',')]) for x in f.readlines()]

memory = set()

size = 70
for y in range(0, size+1):
    for x in range(0, size+1):
        memory.add((x, y))

for block in corrupted:
    memory.remove(block)

    if eval(size, memory):
        print(str(block[0]) + ',' + str(block[1]))
        break
