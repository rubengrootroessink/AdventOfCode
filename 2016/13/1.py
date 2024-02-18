import heapq

def wall(num):
    x, y = num
    curve = x*x + 3*x + 2*x*y + y + y*y
    curve += fav_num
    bin_repr = bin(curve)[2:]

    if sum([1 for x in bin_repr if x == '1']) % 2 == 0:
        return False
    else:
        return True

with open('input.txt') as f:
    fav_num = int(f.read().strip())

heap = [((1, 1), 0)]
short_dist_dict = {(1, 1): 0}

while heap:
    curr_loc, dist = heapq.heappop(heap)

    neighbours = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    neighbours = [(curr_loc[0]+x, curr_loc[1]+y) for (x, y) in neighbours]
    neighbours = [item for item in neighbours if item[0] >= 0 and item[1] >= 0 and not wall(item)]

    for neighbour in neighbours:
        if not neighbour in short_dist_dict.keys() or short_dist_dict[neighbour] > dist + 1:
            short_dist_dict[neighbour] = dist + 1
            heapq.heappush(heap, (neighbour, dist + 1))

print(short_dist_dict[(31, 39)])
