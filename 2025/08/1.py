import heapq
import math

def dist(box1, box2):
    return math.sqrt((box1[0]-box2[0])**2+(box1[1]-box2[1])**2+(box1[2]-box2[2])**2)

with open('input.txt') as f:
    boxes = [tuple(map(int, x.strip().split(','))) for x in f.readlines()]

number_of_boxes = 1000

box_dict = {}

box_pairs = []
for i, box1 in enumerate(boxes):
    box_dict[box1] = []
    for box2 in boxes[i+1:]:
        box_pairs.append((box1, box2, dist(box1, box2)))

box_pairs = sorted(box_pairs, key=lambda x: x[2])[:number_of_boxes]

for (box1, box2, d) in box_pairs:
    box_dict[box1].append(box2)
    box_dict[box2].append(box1)

visited = set()
circuit_dict = {}
for key in boxes:
    if not key in visited:
        circuit = {key}

        visited.add(key)
        
        queue = box_dict[key]
        while queue:
            node = heapq.heappop(queue)
            if not node in visited:
                visited.add(node)
                circuit.add(node)
                for val in box_dict[node]:
                    queue.append(val)

        circuit_dict[tuple(circuit)] = len(circuit)

print(math.prod(sorted(circuit_dict.values())[::-1][0:3]))
