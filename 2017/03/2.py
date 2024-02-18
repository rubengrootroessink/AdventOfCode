with open('input.txt') as f:
    data_loc = int(f.read())

directions = ['east', 'north', 'west', 'south']

loc = (0, 0)
direction = 'east'

locs = {
    (0, 0): 1,
}

found = False
while not found:
    if direction == 'east':
        loc = (loc[0]+1, loc[1])
    elif direction == 'north':
        loc = (loc[0], loc[1]-1)
    elif direction == 'west':
        loc = (loc[0]-1, loc[1])
    elif direction == 'south':
        loc = (loc[0], loc[1]+1)

    val = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if (loc[0]+i, loc[1]+j) in locs.keys():
                    val += locs[(loc[0]+i, loc[1]+j)]

    if val > data_loc:
        found = True
        print(val)

    locs[loc] = val

    n_loc = loc
    if direction == 'east':
        n_loc = (loc[0], loc[1]-1)
    elif direction == 'north':
        n_loc = (loc[0]-1, loc[1])
    elif direction == 'west':
        n_loc = (loc[0], loc[1]+1)
    elif direction == 'south':
        n_loc = (loc[0]+1, loc[1])
    
    if not n_loc in locs.keys():
        direction = directions[(directions.index(direction)+1)%4]
