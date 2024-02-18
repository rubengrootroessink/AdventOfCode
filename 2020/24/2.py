def count_black(x, y, black_tiles):
    count = 0
    if str(x-1) + "/" + str(y-1) in black_tiles.keys():
        count += 1
    if str(x-1) + "/" + str(y+1) in black_tiles.keys():
        count += 1
    if str(x) + "/" + str(y-2) in black_tiles.keys():
        count += 1
    if str(x) + "/" + str(y+2) in black_tiles.keys():  
        count += 1
    if str(x+1) + "/" + str(y-1) in black_tiles.keys():
        count += 1
    if str(x+1) + "/" + str(y+1) in black_tiles.keys(): 
        count += 1
    return count

def simulate_day(black_tiles):
    new_black_tiles = black_tiles.copy()
    for key, value in black_tiles.items():
        adjacent_blacks = count_black(value['x'], value['y'], black_tiles)
        if adjacent_blacks == 0 or adjacent_blacks > 2:
            new_black_tiles.pop(key)
            
        x, y = value['x'], value['y']
        
        for pair in [(-1, -1), (-1, 1), (0, 2), (1, 1), (1, -1), (0, -2)]:
            new_x, new_y = x+pair[0], y+pair[1]
            new_label = str(new_x) + "/" + str(new_y)
            if not new_label in black_tiles.keys():
                adjacent_blacks = count_black(new_x, new_y, black_tiles)
                if adjacent_blacks == 2:
                    new_black_tiles[new_label] = {'x': new_x, 'y': new_y}
            
    return new_black_tiles

instructions = []
with open('input.txt', 'r') as file:    
    for line in file.readlines():
        data = line.split('\n')[0]
        curr_char = 0
        instruction_set = []
        while curr_char < len(data):
            if data[curr_char] == 'n' or data[curr_char] == 's':
                instruction_set.append(data[curr_char:curr_char+2])
                curr_char += 2
            else:
                instruction_set.append(data[curr_char])
                curr_char += 1
        instructions.append(instruction_set)
        
black_tiles = {}
for instruction_set in instructions:
    x, y = 0, 0
    for instruction in instruction_set:
        if instruction == 'nw':
            x, y = x-1, y-1
        elif instruction == 'ne':
            x, y = x-1, y+1
        elif instruction == 'e':
            y = y+2
        elif instruction == 'se':
            x, y = x+1, y+1
        elif instruction == 'sw':
            x, y = x+1, y-1
        elif instruction == 'w':
            y = y-2

    label = str(x) + "/" + str(y)
    if label in black_tiles.keys():
        black_tiles.pop(label)
    else:
        black_tiles[label] = {'x': x, 'y': y}

for i in range(0, 100):
    black_tiles = simulate_day(black_tiles)
print(len(black_tiles))

