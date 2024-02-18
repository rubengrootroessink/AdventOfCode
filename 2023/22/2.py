import heapq

with open('input.txt') as f:
    bricks = [x.split('\n')[0] for x in f.readlines()]

parsed_bricks = []
for brick in bricks:
    p_a, p_b = [[int(y) for y in x.split(',')] for x in brick.split('~')]
    parsed_bricks.append((p_a, p_b))

parsed_bricks = sorted(parsed_bricks, key=lambda x: (x[0][2], x[1][2]))

brick_locs = {}
for i, brick in enumerate(parsed_bricks):
    (x_a, y_a, z_a), (x_b, y_b, z_b) = brick
    all_points = []
    for x in range(x_a, x_b+1):
        for y in range(y_a, y_b+1):
            for z in range(z_a, z_b+1):
                all_points.append((x, y, z))

    stable = False
    while not stable:
        if any([z == 1 for (x,y,z) in all_points]):
            for p in all_points:
                brick_locs[p] = i
            stable = True
        else:
            new_points = [(x,y,z-1) for (x,y,z) in all_points]
            if set(new_points).intersection(brick_locs.keys()):
                for p in all_points:
                    brick_locs[p] = i
                stable = True
            else:
                all_points = new_points

connection_dict = {}

result = 0
for i in range(len(parsed_bricks)):
    points = [(x,y,z) for (x,y,z),val in brick_locs.items() if val == i]
    points_below = [(x,y,z-1) for (x,y,z) in points]
    bricks_below = set()
    for p in points_below:
        if p in brick_locs.keys() and not brick_locs[p] == i:
            bricks_below.add(brick_locs[p])
    
    points_above = [(x,y,z+1) for (x,y,z) in points]
    bricks_above = set()
    for p in points_above:
        if p in brick_locs.keys() and not brick_locs[p] == i:
            bricks_above.add(brick_locs[p])

    connection_dict[i] = {'below': bricks_below, 'above': bricks_above}

result += 0
for i in connection_dict.keys():
    supports = connection_dict[i]['above']
    if len(supports) == 0:
        pass
    elif any([len(connection_dict[j]['below']) < 2 for j in supports]):
        desintegrated = {i}

        heap = list(supports)
        while heap:
            b = heapq.heappop(heap)
            if len(connection_dict[b]['below'] - desintegrated) == 0:
                desintegrated.add(b)

                b_supps = connection_dict[b]['above']

                for s in b_supps:
                    if not s in heap:
                        heapq.heappush(heap, s)

        result += len(desintegrated)-1

print(result)
