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

def print_resting(max_y, resting_blocks):
    board = []
    for y in range(0, max_y+3):
        board.append(list('|.......|'))
    
    for item in resting_blocks:
        board[item[1]][item[0]] = '#'

    for line in board[::-1]:
        print(''.join(line))

with open('input.txt', 'r') as f:
    instrs = list(f.read().split()[0])

resting_blocks = set()

block_counter = 0
instr_counter = 0

max_y = 0

configs = []

j = 0
while True:
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

    config = (block_counter, instr_counter)
    if [y for (x,y) in configs].count(config) == 3:

        earlier = [x for (x,y) in configs if y == config]
        
        height_end, cycle_end = earlier[2]
        height_start, cycle_start = earlier[1]
        
        height_diff = height_end - height_start
        cycle_diff = cycle_end - cycle_start
        
        nr_cycles = 1000000000000-1
        nr_cycles = nr_cycles - earlier[2][1]
        
        nr_cycles_skipped = nr_cycles // cycle_diff
        nr_cycles_left = nr_cycles % cycle_diff

        remaining_height = configs[cycle_start+nr_cycles_left][0][0] - height_start
        base_calc = earlier[2][0] + nr_cycles_skipped * height_diff + remaining_height
        
        print(base_calc)

        break
    else:
        configs.append(((max_y, j), config))
    j += 1
