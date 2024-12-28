from collections import defaultdict, deque
import math

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

board = defaultdict(bool)

for y, row in enumerate(rows):
    for x, column in enumerate(row):
        if column == '#':
            board[(x, y)] = True

asteroids = list(board.keys())

max_val = 0
loc_station = None

for station in asteroids:
    count = 0
    for asteroid in asteroids:
        if station == asteroid:
            continue

        slope_x = asteroid[0]-station[0]
        slope_y = asteroid[1]-station[1]

        if slope_x == 0: # They are above one another

            high, low = station, asteroid
            if high[1] < low[1]:
                tmp = high
                high = low
                low = tmp

            intersecting = []
            for i in range(low[1]+1, high[1]):
                intersecting.append((low[0], i))

            intersecting = [x for x in intersecting if x in asteroids]
            if len(intersecting) == 0:
                count += 1

        elif slope_x != 0:
            m = slope_y / slope_x
            
            high, low = station, asteroid
            if high[0] < low[0]:
                tmp = high
                high = low
                low = tmp
        
            intersecting = []
            curr = low
            while curr != high:
                curr = (curr[0]+1, curr[1]+m)
                if abs(curr[1] - round(curr[1])) < 0.00001: # Floating point arithmetic rounding errors
                    curr = (curr[0], round(curr[1]))
                    intersecting.append(curr)

            intersecting = intersecting[:-1]
            intersecting = [x for x in intersecting if x in asteroids]

            if len(intersecting) == 0:
                count += 1

    if count > max_val:
        loc_station = station
        max_val = count

vaporize_order = []
for asteroid in asteroids:
    if asteroid == loc_station:
        continue

    x_diff = asteroid[0]-loc_station[0]
    y_diff = asteroid[1]-loc_station[1]

    angle = math.degrees(math.atan2(y_diff, x_diff))+90
    if angle < 0:
        angle += 360

    vaporize_order.append((asteroid, angle, abs(loc_station[0]-asteroid[0])+abs(loc_station[1]-asteroid[1])))

vaporize_order = list(sorted(vaporize_order, key=lambda x: (x[1], -x[2])))

order = 1
queue = deque(vaporize_order)

while queue:

    loc, angle, man_dist = queue.popleft()

    intersections = [x for x in queue if x[1] == angle]

    intersected = False
    for o_loc, _, _ in intersections:
        x_vals = [loc_station[0], loc[0]]
        min_x, max_x = min(x_vals), max(x_vals)
        y_vals = [loc_station[1], loc[1]]
        min_y, max_y = min(y_vals), max(y_vals)
        if o_loc[0] in range(min_x, max_x+1) and o_loc[1] in range(min_y, max_y+1):
            intersected = True

    if intersected:
        queue.append((loc, angle, man_dist))
    else:
        if order == 200:
            print(loc[0]*100+loc[1])
            break

        order += 1

