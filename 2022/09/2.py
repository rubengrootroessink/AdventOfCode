with open('input.txt', 'r') as f:
    instrs = [x.split('\n')[0].split(' ') for x in f.readlines()]
    instrs = [(x[0], int(x[1])) for x in instrs]

def change_val(pos_prev, item, direction):
    if (abs(pos_prev[0]-item[0]) <= 1 and abs(pos_prev[1]-item[1]) <= 1):
        pass
    elif (abs(pos_prev[0]-item[0]) == 2 and abs(pos_prev[1]-item[1]) == 2):
        item_next = (item[0]+(pos_prev[0]-item[0])//2, item[1]+(pos_prev[1]-item[1])//2)
        return item_next
    elif (abs(pos_prev[0]-item[0]) == 2 and abs(pos_prev[1]-item[1]) == 1):
        item_next = (item[0]+(pos_prev[0]-item[0])//2, pos_prev[1])
        return item_next
    elif (abs(pos_prev[0]-item[0]) == 1 and abs(pos_prev[1]-item[1]) == 2):
        item_next = (pos_prev[0], item[1]+(pos_prev[1]-item[1])//2)
        return item_next
    elif abs(pos_prev[0]-item[0]) == 2:
        item_next = (item[0]+(pos_prev[0]-item[0])//2, item[1])
        return item_next
    elif abs(pos_prev[1]-item[1]) == 2:
        item_next = (item[0], item[1]+(pos_prev[1]-item[1])//2)
        return item_next
    
    return item

tail_positions = [(0,0)]

knots = [(0,0)]*10

for instr in instrs:
    direction, amount = instr
    for i in range(0, amount):
        
        if direction == 'R':
            knots[0] = (knots[0][0]+1, knots[0][1])
        elif direction == 'L':
            knots[0] = (knots[0][0]-1, knots[0][1])
        elif direction == 'U':
            knots[0] = (knots[0][0], knots[0][1]+1)
        elif direction == 'D':
            knots[0] = (knots[0][0], knots[0][1]-1)

        pos_prev = knots[0]
        for i, item in enumerate(knots[1:]):
            new_val = change_val(pos_prev, item, direction)
            knots[i+1] = new_val
            pos_prev = knots[i+1]

        tail_positions.append(knots[-1])

print(len(set(tail_positions)))
