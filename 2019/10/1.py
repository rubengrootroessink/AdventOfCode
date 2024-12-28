from collections import defaultdict

with open('input.txt') as f:
    rows = [x.strip() for x in f.readlines()]

board = defaultdict(bool)

for y, row in enumerate(rows):
    for x, column in enumerate(row):
        if column == '#':
            board[(x, y)] = True

asteroids = list(board.keys())

max_val = 0

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

    max_val = max(max_val, count)

print(max_val)
