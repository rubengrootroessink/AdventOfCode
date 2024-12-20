from collections import defaultdict
import heapq

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

board = defaultdict(str)
start = None
end = None
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        board[(i, j)] = column
        if column == 'S':
            start = (i, j)
        elif column == 'E':
            end = (i, j)

queue = [([], end)]
visited = {end}
dist_dict = {}
neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start_path = None
while queue:
    path, node = heapq.heappop(queue)
    ns = [(node[0]+n[0], node[1]+n[1]) for n in neighbours]
    ns = [n for n in ns if not board[n] in ['', '#']]

    if node == start:
        start_path = path + [node]
        start_path = start_path[::-1]

    for n in ns:
        if not n in visited:
            visited.add(n)
            dist_dict[n] = len(path) + 1
            heapq.heappush(queue, (path + [node], n))

    queue = sorted(queue, key=lambda x: len(x[0]))

dist = dist_dict[start]
dist_dict[end] = 0

matching_cheats = defaultdict(int)
for i, node in enumerate(start_path):
    for n in neighbours:
        n1 = (node[0]+n[0], node[1]+n[1])
        n2 = (node[0]+2*n[0], node[1]+2*n[1])

        if board[n1] == '#' and board[n2] in ['.', 'E']:
            new_dist = i + 2 + dist_dict[n2]

            if new_dist < dist-99:
                matching_cheats[dist-new_dist] += 1

print(sum(matching_cheats.values()))
