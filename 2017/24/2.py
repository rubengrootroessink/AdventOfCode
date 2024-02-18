import heapq

with open('input.txt') as f:
    dominos = [tuple([int(y) for y in x.strip().split('/')]) for x in f.readlines()]

bridges = []

start_dominos = [d for d in dominos if d[0] == 0 or d[1] == 0]

heap = [([d], max(d)) for d in start_dominos]
while heap:
    path, head = heapq.heappop(heap)
    bridges.append(path)

    adjacent_dominos = [d for d in dominos if (d[0] == head or d[1] == head) and not d in path]

    for d in adjacent_dominos:
        new_head = [x for x in d if x != head][0] if d[0] != d[1] else d[0]
        heapq.heappush(heap, (path + [d], new_head))

longest_size = max([len(x) for x in bridges])

max_strength = 0
for bridge in bridges:
    curr_count = 0
    for elem in bridge:
        curr_count += elem[0]+elem[1]

    if len(bridge) == longest_size:
        max_strength = max(max_strength, curr_count)

print(max_strength)
