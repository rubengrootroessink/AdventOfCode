from collections import defaultdict
from itertools import permutations
import heapq

inpt = []

def resolve(mode, offset, rel_base, instrs):
    if mode == 0:
        return instrs[instrs[offset]]
    elif mode == 1:
        return instrs[offset]
    elif mode == 2:
        return instrs[rel_base+instrs[offset]]

def run(instrs):
    eip = 0

    rel_base = 0
    output = []
    
    finished = False
    while not finished:
        op_num = instrs[eip]
        op_code = op_num % 100

        modes = (op_num - op_code) // 100
        mode_1 = modes % 10
        mode_2 = ((modes - mode_1) // 10) % 10
        mode_3 = ((modes - mode_1 - mode_2 * 10) // 100) % 100

        eip_jumps = 2

        match op_code:
            case 1 | 2 | 7 | 8:

                val_1 = resolve(mode_1, eip+1, rel_base, instrs)
                val_2 = resolve(mode_2, eip+2, rel_base, instrs)

                res = 0
                
                if op_code == 1:
                    res = val_1 + val_2
                elif op_code == 2:
                    res = val_1 * val_2
                elif op_code == 7:
                    res = 1 if val_1 < val_2 else 0
                elif op_code == 8:
                    res = 1 if val_1 == val_2 else 0
                
                if mode_3 == 0:
                    instrs[instrs[eip+3]] = res
                elif mode_3 == 1:
                    instrs[eip+3] = res
                elif mode_3 == 2:
                    instrs[rel_base+instrs[eip+3]] = res
                
                eip_jumps += 2

            case 3:
                
                if mode_1 == 0:
                    instrs[instrs[eip+1]] = heapq.heappop(inpt)
                elif mode_1 == 1:
                    instrs[eip+1] = heapq.heappop(inpt)
                elif mode_1 == 2:
                    instrs[rel_base+instrs[eip+1]] = heapq.heappop(inpt)
                    
            case 4:

                val_1 = resolve(mode_1, eip+1, rel_base, instrs)
                yield val_1

            case 5 | 6:
                
                val_1 = resolve(mode_1, eip+1, rel_base, instrs)
                val_2 = resolve(mode_2, eip+2, rel_base, instrs)

                if op_code == 5 and val_1 != 0:
                    eip = val_2
                    eip_jumps = 0
                elif op_code == 6 and val_1 == 0:
                    eip = val_2
                    eip_jumps = 0
                else:
                    eip_jumps += 1

            case 9:

                val_1 = resolve(mode_1, eip+1, rel_base, instrs)
                rel_base += val_1

            case 99:

                finished = True

        eip += eip_jumps

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = defaultdict(int)
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

instr_dict[0] = 2

robot = run(instr_dict)
loc_dict = defaultdict(int)

# Build Phase
while True:
    try:
        x = next(robot)
        y = next(robot)
        tile_id = next(robot)

        if x == -1 and y == 0:
            break
        else:
            loc_dict[(x, y)] = tile_id
    except:
        pass

paddle_loc = [x for x in loc_dict.items() if x[1] == 3][0][0]
loc_dict[paddle_loc] = 0

paddle_x, paddle_y = paddle_loc

score = 0

found = False

# Run Phase
while not found:
    ball = [x for x in loc_dict.items() if x[1] == 4][0][0]
    last_ball = (ball[0]-1, ball[1]-1)

    num_moves = 0

    if not paddle_x in range(ball[0]-1, ball[0]+2):

        intersection = ball
        while intersection[1] != 19:
            intersection = (intersection[0]+(ball[0]-last_ball[0]), intersection[1]+(ball[1]-last_ball[1]))

        if paddle_x < intersection[0]:
            inpt.append(1)
            num_moves = 4
            paddle_x += 1
        elif paddle_x > intersection[0]:
            inpt.append(-1)
            num_moves = 4
            paddle_x -= 1
        else:
            inpt.append(0)
            num_moves = 2
    else:
        if paddle_x == ball[0] + 1:
            inpt.append(-1)
            num_moves = 4
            paddle_x -= 1
        elif paddle_x == ball[0] - 1:
            inpt.append(1)
            num_moves = 4
            paddle_x += 1
        else:
            inpt.append(0)
            num_moves = 2
    
    count = 0
    while count < num_moves:
        try:
            x = next(robot)
            y = next(robot)
            tile_id = next(robot)
            if (x, y) == (-1, 0):
                score = tile_id
                num_moves += 1
            else:
                if tile_id != 3:
                    loc_dict[(x, y)] = tile_id
                count += 1
        except:
            print(score)
            found = True
            break

    last_ball = ball
