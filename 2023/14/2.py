import json
import copy
import hashlib

def tilt(rocks, x_dir, y_dir):

    if y_dir == -1: # Northern tilt
        sorted_rocks = {key: value for key, value in sorted(rocks.items(), key = lambda x: x[0][1])}
    elif y_dir == 1: # Southern tilt
        sorted_rocks = {key: value for key, value in sorted(rocks.items(), key = lambda x: -x[0][1])}
    elif x_dir == -1: # Western tilt
        sorted_rocks = {key: value for key, value in sorted(rocks.items(), key = lambda x: x[0][0])}
    elif x_dir == 1: # Eastern tilt
        sorted_rocks = {key: value for key, value in sorted(rocks.items(), key = lambda x: -x[0][0])}

    new_rocks = {}
    for key, value in sorted_rocks.items():

        if value == '#':
            new_rocks[key] = value

        elif value == 'O':
            new_key = (key[0]+x_dir, key[1]+y_dir)
            if (not 0<=new_key[0]<max_x or not 0<=new_key[1]<max_y): # Case: Outside of boundaries
                new_rocks[key] = value
            elif (y_dir == -1 and new_key[1] == 0) and not new_key in new_rocks.keys(): # Northern tilt
                new_rocks[new_key] = value
            elif (y_dir == 1 and new_key[1] == max_y-1) and not new_key in new_rocks.keys(): # Southern tilt
                new_rocks[new_key] = value
            elif (x_dir == -1 and new_key[0] == 0) and not new_key in new_rocks.keys(): # Western tilt
                new_rocks[new_key] = value
            elif (x_dir == 1 and new_key[0] == max_x-1) and not new_key in new_rocks.keys(): # Eastern tilt
                new_rocks[new_key] = value
            elif new_key in new_rocks.keys():
                new_rocks[key] = value            

            while (0<=new_key[0]<max_x and 0<=new_key[1]<max_y) and not new_key in new_rocks.keys():
                new_key = (new_key[0]+x_dir, new_key[1]+y_dir)
                if (y_dir == -1 and new_key[1] == 0) and not new_key in new_rocks.keys(): # Northern tilt
                    new_rocks[new_key] = value
                elif (y_dir == 1 and new_key[1] == max_y-1) and not new_key in new_rocks.keys(): # Southern tilt
                    new_rocks[new_key] = value
                elif (x_dir == -1 and new_key[0] == 0) and not new_key in new_rocks.keys(): # Western tilt
                    new_rocks[new_key] = value
                elif (x_dir == 1 and new_key[0] == max_x-1) and not new_key in new_rocks.keys(): # Eastern tilt
                    new_rocks[new_key] = value
                elif new_key in new_rocks.keys():
                    new_rocks[(new_key[0]+(0-x_dir), new_key[1]+(0-y_dir))] = value

    return new_rocks

def spin_cycle(rocks):
    new_rocks = tilt(rocks, 0, -1)
    new_rocks = tilt(new_rocks, -1, 0)
    new_rocks = tilt(new_rocks, 0, 1)
    new_rocks = tilt(new_rocks, 1, 0)
    return new_rocks

with open('input.txt') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

rocks = {}
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column in ['#', 'O']:
            rocks[(i, j)] = column

max_y = len(rows)
max_x = len(rows[0])

new_rocks = rocks
hash_dict = {}

found = False
i = 0
cycle_start, cycle_length = 0, 0
while not found:
    new_rocks = spin_cycle(new_rocks)
    md5_hash = hashlib.md5(str(sorted(new_rocks.items())).encode('utf-8')).digest()
    if md5_hash in hash_dict.keys():
        val = hash_dict[md5_hash]
        if len(val) == 3:
            found = True
            cycle_start = val[0]
            cycle_length = val[-1] - val[-2]
        else:
            hash_dict[md5_hash].append(i)
    else:
        hash_dict[md5_hash] = [i]
    i += 1

total_length = 1000000000
total_length = (total_length - cycle_start) % cycle_length + cycle_start

new_rocks = rocks
for i in range(total_length):
    new_rocks = spin_cycle(new_rocks)

num_rows = len(row)
result = sum([num_rows-k[1] for k, v in new_rocks.items() if v == 'O'])

print(result)
