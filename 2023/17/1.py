# Inspired by others

import sys
import heapq

def a_star(city_blocks):
    start_node, end_node = (0,0), (max_x-1,max_y-1)

    heap, visited = [(0,-1,-1,) + start_node], {}

    while heap:

        count, direction, direction_count, x, y = heapq.heappop(heap)
        
        if (x, y, direction, direction_count) in visited:
            continue

        visited[(x, y, direction, direction_count)] = count
        
        neighbours = [
            (x-1, y), # Direction 0
            (x, y+1), # Direction 1
            (x+1, y), # Direction 2
            (x, y-1), # Direction 3
        ]

        for i, (dx, dy) in enumerate(neighbours):
            
            if 0<=dx<max_x and 0<=dy<max_y: # Otherwise outside of range

                new_direction = i
                new_direction_count = (1 if new_direction != direction else direction_count+1)

                if new_direction_count <= 3: # Inside the boundaries set by the assignment

                    if ((new_direction + 2) % 4 != direction): # Not reverse direction
                        heapq.heappush(heap, (count + city_blocks[dy][dx], new_direction, new_direction_count, dx, dy))

    result = sys.maxsize
    for (x, y, direction, direction_count), count in visited.items():
        if (x,y) == end_node:
            result = min(result, count)
    return result

with open('input.txt') as f:
    city_blocks = [list(map(lambda x: int(x), line.strip())) for line in f.readlines()]
    max_y = len(city_blocks)
    max_x = len(city_blocks[0])

print(a_star(city_blocks))

