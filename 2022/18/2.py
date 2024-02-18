import copy

with open('input.txt', 'r') as f:
    blocks = [tuple([int(y) for y in x.split('\n')[0].split(',')]) for x in f.readlines()]

x_coords = [block[0] for block in blocks]
min_x = min(x_coords)
max_x = max(x_coords)+1

y_coords = [block[1] for block in blocks]
min_y = min(y_coords)
max_y = max(y_coords)+1

z_coords = [block[2] for block in blocks]
min_z = min(z_coords)
max_z = max(z_coords)+1

coordinate_dict = {}
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        for k in range(min_z, max_z):
            if (i,j,k) in blocks:
                coordinate_dict[(i,j,k)] = 'lava'
            elif i == min_x or i == max_x-1 or j == min_y or j == max_y-1 or k == min_z or k == max_z-1:
                coordinate_dict[(i,j,k)] = 'water'
            else:
                coordinate_dict[(i,j,k)] = 'unknown'

while True:
    changed = False

    new_dict = copy.deepcopy(coordinate_dict)
    unknowns = [key for key, value in coordinate_dict.items() if value == 'unknown']

    for unknown in unknowns:
        x_border_left = (unknown[0]-1, unknown[1], unknown[2])
        x_border_right = (unknown[0]+1, unknown[1], unknown[2])
        y_border_left = (unknown[0], unknown[1]-1, unknown[2])
        y_border_right = (unknown[0], unknown[1]+1, unknown[2])
        z_border_left = (unknown[0], unknown[1], unknown[2]-1)
        z_border_right = (unknown[0], unknown[1], unknown[2]+1)

        bordering = [
            coordinate_dict[x_border_left],
            coordinate_dict[x_border_right],
            coordinate_dict[y_border_left],
            coordinate_dict[y_border_right],
            coordinate_dict[z_border_left],
            coordinate_dict[z_border_right],
        ]

        water_nearby = [x == 'water' for x in bordering]

        if any(water_nearby):
            new_dict[unknown] = 'water'
            changed = True

    if not changed:
        break

    coordinate_dict = new_dict

blocks = [key for key, value in coordinate_dict.items() if value == 'lava' or value == 'unknown']

total_sides = len(blocks)*6
for i, block in enumerate(blocks):
    for other_block in blocks[i+1:]:
        if abs(block[0]-other_block[0]) == 1 and block[1] == other_block[1] and block[2] == other_block[2]:
            total_sides -= 2
        if abs(block[1]-other_block[1]) == 1 and block[0] == other_block[0] and block[2] == other_block[2]:
            total_sides -= 2
        if abs(block[2]-other_block[2]) == 1 and block[0] == other_block[0] and block[1] == other_block[1]:
            total_sides -= 2

print(total_sides)
