from collections import defaultdict
import heapq
import math

def dist(box1, box2):
    return math.sqrt((box1[0]-box2[0])**2+(box1[1]-box2[1])**2+(box1[2]-box2[2])**2)

with open('input.txt') as f:
    boxes = [tuple(map(int, x.strip().split(','))) for x in f.readlines()]

box_pairs = []
for i, box1 in enumerate(boxes):
    for box2 in boxes[i+1:]:
        box_pairs.append((box1, box2, dist(box1, box2)))

box_pairs = sorted(box_pairs, key=lambda x: x[2])

min_val = 0
max_val = len(box_pairs)

split_val = min_val + ((max_val - min_val) // 2)

while True:
    edge_dict = defaultdict(set)

    for (box1, box2, _) in box_pairs[:split_val]:
        edge_dict[box1].add(box2)
        edge_dict[box2].add(box1)

    start_node = list(edge_dict.keys())[0]
    queue = [start_node]
    visited = {start_node}
    while queue:
        node = heapq.heappop(queue)

        for neighbour in edge_dict[node]:
            if not neighbour in visited:
                visited.add(neighbour)
                heapq.heappush(queue, neighbour)

    if len(visited) == len(boxes):
        max_val = split_val
    else:
        min_val = split_val
    split_val = min_val + ((max_val - min_val) // 2)

    if min_val == split_val or max_val == split_val:
        box1, box2, _ = box_pairs[split_val]
        print(box1[0] * box2[0])
        break
