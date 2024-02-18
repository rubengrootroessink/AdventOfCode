with open('input.txt') as f:
    data_loc = int(f.read())

directions = ['east', 'north', 'west', 'south']

loc = (0, 0)
direction = 'east'

locs = {
    (0, 0): 1,
}

for n in range(1, data_loc):
    if direction == 'east':
        loc = (loc[0]+1, loc[1])
    elif direction == 'north':
        loc = (loc[0], loc[1]-1)
    elif direction == 'west':
        loc = (loc[0]-1, loc[1])
    elif direction == 'south':
        loc = (loc[0], loc[1]+1)

    locs[loc] = n+1

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

print(abs(loc[0]) + abs(loc[1]))
