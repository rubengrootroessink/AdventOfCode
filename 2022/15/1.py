import re

def merge_ranges(x, y):
    if x.start == y.start:
        return [range(x.start, y.stop)]
    elif x.stop < y.start:
        return [x, y]
    elif x.start < y.start:
        return [range(x.start, max(x.stop, y.stop))]
    else:
        assert False

def find_vals(line):
    pattern = r'Sensor at x=([-]{0,1}\d+), y=([-]{0,1}\d+): closest beacon is at x=([-]{0,1}\d+), y=([-]{0,1}\d+)'
    matcher = re.match(pattern, line)
    return [int(x) for x in matcher.groups()]

with open('input.txt', 'r') as f:
    data = [find_vals(x.split('\n')[0]) for x in f.readlines()]

result_list = []
beacon_list = []

check_line = 2000000

sensor_ranges = []

for item in data:
    sensor, beacon = item[0:2], item[2:4]
    
    if beacon[1] == check_line:
        beacon_list.append((beacon[0], beacon[1]))

    mnhtn_dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

    j = mnhtn_dist - abs(check_line - sensor[1])

    if j >= 0:
        sensor_range = range(sensor[0]-j, sensor[0]+j+1)
        sensor_ranges.append(sensor_range)

sensor_ranges = sorted(sensor_ranges, key=lambda x: (x.start, x.stop))

found = False
start_index = 0
while not found:
    left, right = sensor_ranges[start_index:start_index+2]
    result = merge_ranges(left, right)
    
    if len(result) > 1:
        start_index += 1
    sensor_ranges = result + sensor_ranges[start_index+2:]

    if start_index >= len(sensor_ranges) or len(sensor_ranges) == 1:
        found = True

print(sum([len(x) for x in sensor_ranges]) - len(set(beacon_list)))
