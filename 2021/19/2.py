from itertools import zip_longest

def rotate_once(x, y, z, orient):
    if orient == 'x':
        return x, -z, y
    elif orient == 'y':
        return z, y, -x

def rotate_chain(instrs, x, y, z):
    if len(instrs) == 1:
        return rotate_once(x, y, z, instrs[0])
    new_x, new_y, new_z = rotate_once(x, y, z, instrs[0])
    return rotate_chain(instrs[1:], new_x, new_y, new_z)

rotations = [
    'x',    'xx',  'xxx',
    'y',    'yy',  'yyy',
    'xy',   'xyy', 'xyyy',
    'xxy',  'xxyy', 
    'xxxy', 'xxxyx',
    'xxxyy',
    'yx',   'yxx', 'yxxx',
    'xyx',  'xyxy',
    'yyyx',
    'yxyx',
    'xyxxx',
    'xyyyx',
]

def find_edges(beacon_set):
    dict_edges = {}
    set_edges = set()
    for x1, y1, z1 in beacon_set:
        for x2, y2, z2 in beacon_set:
            if (x1,y1,z1) in dict_edges.keys():
                dict_edges[(x1,y1,z1)] = dict_edges[(x1,y1,z1)] + [(x1-x2, y1-y2, z1-z2)]
            else:
                dict_edges[(x1,y1,z1)] = [(x1-x2,y1-y2,z1-z2)]
            set_edges.add((x1-x2,y1-y2,z1-z2))
    return dict_edges, set_edges

def rotate(scanner_vals):
    beacons = []
    for (x, y, z) in scanner_vals:
        result = [(x,y,z)]
        for rot in rotations:
            result.append(rotate_chain(rot, x, y, z))
        beacons.append(result)
    beacons = list(zip_longest(*beacons, fillvalue=None))
    return beacons

def find_match(start_set_edges, beacon_configs):
    for poss in beacon_configs:
        new_dict_edges, new_set_edges = find_edges(poss)
        if len(start_set_edges & new_set_edges) >= 66:
            return poss, new_dict_edges
    else:
        return False

def get_new_edges(new_dict_edges, start_set_edges, start_dict_edges):
    new_keys = []
    offset = []

    for key1, value1 in new_dict_edges.items():
        filtered_edges = [x for x in value1 if x in start_set_edges]
        if len(filtered_edges) >= 12 and offset == []:
            for key2, value2 in start_dict_edges.items():
                if all([x in value2 for x in filtered_edges]):
                    offset = [key1[0]-key2[0],key1[1]-key2[1],key1[2]-key2[2]]
        elif len(filtered_edges) == 1:
            new_keys.append(key1)

    if offset == []:
        return False

    return [(x[0]-offset[0],x[1]-offset[1],x[2]-offset[2]) for x in new_keys], [-x for x in offset]

def manhattan(a, b):
    return sum([abs(x-y) for x,y in zip(a,b)])

scanners = {}
with open('input.txt') as f:
    data = f.read().split('\n\n--- scanner ')
    for i, scanner_data in enumerate(data):
        values = [[int(y) for y in x.split(',')] for x in scanner_data.split('\n')[1:] if x != '']
        scanners[i] = values

f_scanner = scanners[0]
o_scanners = set(list(scanners.keys())[1:])

start_dict_edges, start_set_edges = find_edges(f_scanner)

offsets = []
for i in range(0, len(o_scanners)):
    scans = list(o_scanners)
    for scan in scans:
        beacon_configs = rotate(scanners[scan])
        val = find_match(start_set_edges, beacon_configs)
        if val:
            right_rotation, new_dict_edges = val
            new_values = get_new_edges(new_dict_edges, start_set_edges, start_dict_edges)
            if new_values:
                new_points, offset = new_values
                offsets.append(offset)
                scanners[0] = scanners[0] + new_points
                o_scanners.remove(scan)
                start_dict_edges, start_set_edges = find_edges(scanners[0])
                break

max_offset = 0
for i, a in enumerate(offsets):
    for b in offsets[i+1:]:
        dist = manhattan(a,b)
        if dist > max_offset:
            max_offset = dist

print(max_offset)
