import re
import copy

def find_vals(line):
    pattern = r'Sensor at x=([-]{0,1}\d+), y=([-]{0,1}\d+): closest beacon is at x=([-]{0,1}\d+), y=([-]{0,1}\d+)'
    matcher = re.match(pattern, line)
    return [int(x) for x in matcher.groups()]

def check(poss_val, diamonds):
    for (sensor, mnhtn_dist) in diamonds:
        new_mnhtn_dist = abs(sensor[0]-poss_val[0]) + abs(sensor[1]-poss_val[1])
        if new_mnhtn_dist <= mnhtn_dist:
            return False
    return True

with open('input.txt', 'r') as f:
    data = [find_vals(x.split('\n')[0]) for x in f.readlines()]

result_list = []
beacon_list = []

sensor_ranges = []

diamonds = []

max_val = 4000000

edges = set()
for item in data:
    sensor, beacon = item[0:2], item[2:4]
    beacon_list.append((beacon[0], beacon[1]))

    mnhtn_dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

    start_x, y = sensor[0], sensor[1]+mnhtn_dist+1

    edge = []
    for x in range(start_x, start_x+mnhtn_dist+2):
        edge.append((x, y))
        y -= 1

    for (i, j) in edge:
        mirror_x = sensor[0]-(abs(i-sensor[0]))
        mirror_y = sensor[1]-(abs(j-sensor[1]))

        check_mirror_x = mirror_x >= 0 and mirror_x <= max_val
        check_mirror_y = mirror_y >= 0 and mirror_y <= max_val
        check_i = i >= 0 and i <= max_val
        check_j = j >= 0 and j <= max_val

        if check_mirror_x:
            if check_mirror_y:
                edges.add((mirror_x, mirror_y))
            if check_j:
                edges.add((mirror_x, j))
        if check_i:
            if check_mirror_y:
                edges.add((i, mirror_y))
            if check_j:
                edges.add((i, j))
    
    diamonds.append((sensor, mnhtn_dist))

full_result = set()
for poss_val in edges:
    if check(poss_val, diamonds):
        full_result.add(poss_val)

final_val = list(full_result)[0]
print(final_val[0]*4000000+final_val[1])
