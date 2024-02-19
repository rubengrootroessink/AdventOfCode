import sys

with open('input.txt') as f:
    wire_1, wire_2 = [x.split(',') for x in f.read().strip().split('\n')]

wires_locs = {}

for j, wire in enumerate([wire_1, wire_2]):
    curr_loc = (0, 0)

    locs = [(0, 0)]
    for instr in wire:
        direction, value = instr[0], int(instr[1:])

        match direction:
            case 'R':
                for i in range(value):
                    curr_loc = (curr_loc[0]+1, curr_loc[1])
                    locs.append(curr_loc)

            case 'L':
                for i in range(value):
                    curr_loc = (curr_loc[0]-1, curr_loc[1])
                    locs.append(curr_loc)

            case 'U':
                for i in range(value):
                    curr_loc = (curr_loc[0], curr_loc[1]-1)
                    locs.append(curr_loc)

            case 'D':
                for i in range(value):
                    curr_loc = (curr_loc[0], curr_loc[1]+1)
                    locs.append(curr_loc)

    wires_locs[j] = set(locs)

intersections = wires_locs[0].intersection(wires_locs[1])

closest = sys.maxsize
for inter in [x for x in intersections if not x == (0, 0)]:
    dist = abs(inter[0]) + abs(inter[1])
    closest = min(closest, dist)

print(closest)
