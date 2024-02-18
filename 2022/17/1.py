blocks = [
    [(3,1), (4,1), (5,1), (6,1)],
    [(4,1), (3,2), (4,2), (5,2), (4,3)],
    [(3,1), (4,1), (5,1), (5,2), (5,3)],
    [(3,1), (3,2), (3,3), (3,4)],
    [(3,1), (4,1), (3,2), (4,2)],
]

def eval(movement, block, resting_blocks):
    if movement == 'right':
        moved_block = [(x+1,y) for (x,y) in block]
        if any([x == 8 for (x,y) in moved_block]):
            return block
        elif any([(x,y) in resting_blocks for (x,y) in moved_block]):
            return block
        return moved_block
    elif movement == 'left':
        moved_block = [(x-1,y) for (x,y) in block]
        if any([x == 0 for (x,y) in moved_block]):
            return block
        elif any([(x,y) in resting_blocks for (x,y) in moved_block]):
            return block
        return moved_block
    elif movement == 'down':
        moved_block = [(x, y-1) for (x,y) in block]
        if any([y == 0 for (x,y) in moved_block]):
            return block
        elif any([(x,y) in resting_blocks for (x,y) in moved_block]):
            return block
        return moved_block

with open('input.txt', 'r') as f:
    instrs = list(f.read().split()[0])

resting_blocks = set()

block_counter = 0
instr_counter = 0

max_y = 0
for j in range(0, 2022):
    block = blocks[block_counter]
    block = [(x,max_y+y+3) for (x,y) in block]
    
    resting = False
    while not resting:
        if instrs[instr_counter] == '>':
            shifted_block = eval('right', block, resting_blocks)
        elif instrs[instr_counter] == '<':
            shifted_block = eval('left', block, resting_blocks)

        down_block = eval('down', shifted_block, resting_blocks)
        if down_block == shifted_block:
            resting = True
            resting_blocks = resting_blocks.union(set(down_block))
            max_y = max(max_y, max([y for (x,y) in down_block]))
        else:
            block = down_block

        instr_counter = (instr_counter + 1) % len(instrs)

    block_counter = (block_counter + 1) % len(blocks)

print(max_y)
