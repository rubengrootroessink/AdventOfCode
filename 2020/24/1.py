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
        
print(len(black_tiles))
