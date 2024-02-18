with open('input.txt', 'r') as f:
    blocks = [[int(y) for y in x.split('\n')[0].split(',')] for x in f.readlines()]

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
