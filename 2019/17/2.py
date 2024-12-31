from collections import defaultdict, deque, Counter
from itertools import permutations
import copy

def resolve(mode, offset, rel_base, instrs):
    if mode == 0:
        return instrs[instrs[offset]]
    elif mode == 1:
        return instrs[offset]
    elif mode == 2:
        return instrs[rel_base+instrs[offset]]

def run(instrs, inpt):
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

                input_val = inpt.popleft()

                if mode_1 == 0:
                    instrs[instrs[eip+1]] = input_val
                elif mode_1 == 1:
                    instrs[eip+1] = input_val
                elif mode_1 == 2:
                    instrs[rel_base+instrs[eip+1]] = input_val

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

def digit_count(segment):
    result = 0
    d_count = 0
    for char in segment:
        if not char.isdigit():
            result += d_count + 3
            d_count = 0
        else:
            d_count += 1
    return result

def create_path(segment):
    result = []
    curr_int = ''
    for char in segment:
        if not char.isdigit():
            if curr_int != '':
                result.append(curr_int)
            result.append(char)
            curr_int = ''
        else:
            curr_int += char

    if curr_int != '':
        result.append(curr_int)

    return result

def split_path(path):
    path_string = ''.join([str(x) for x in path])

    a_start = 0
    indices = [i for i, x in enumerate(path_string) if not x.isdigit()][1:] # Omit first value (0)

    for i, a_end in enumerate(indices):
        a_segment = path_string[a_start:a_end]
        a_count = digit_count(a_segment)

        if a_count > 20:
            continue

        for j, b_start in enumerate(indices):
            if j <= i:
                continue
            for k, b_end in enumerate(indices):
                if any(k <= x for x in [i, j]):
                    continue

                b_segment = path_string[b_start:b_end]
                b_count = digit_count(b_segment)

                if b_count > 20:
                    continue

                for l, c_start in enumerate(indices):
                    if any(l <= x for x in [i, j, k]):
                        continue

                    for m, c_end in enumerate(indices):
                        if any(m <= x for x in [i, j, k, l]):
                            continue

                        c_segment = path_string[c_start:c_end]
                        c_count = digit_count(c_segment)

                        if c_count > 20:
                            continue

                        new_path = path_string.replace(a_segment, 'A')
                        new_path = new_path.replace(b_segment, 'B')
                        new_path = new_path.replace(c_segment, 'C')

                        if all([x in ['A', 'B', 'C'] for x in new_path]):
                            return list(new_path), create_path(a_segment), create_path(b_segment), create_path(c_segment)

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = defaultdict(int)
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

inpt = deque([])

robot = run(copy.deepcopy(instr_dict), inpt)

output = ""

while True:
    try:
        output += chr(next(robot))
    except:
        break

board = defaultdict(str)

rows = output.split('\n')
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        board[(i, j)] = column

neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]

curr_pos = [k for k, v in board.items() if v == '^'][0]
direction = 'U'

visited = {curr_pos}

directions = {
    (-1, 0): 'L',
    (1, 0): 'R',
    (0, -1): 'U',
    (0, 1): 'D',
}

dirs = ['L', 'U', 'R', 'D']

path = []
count = 0

intersections = set()

while True:

    ns = [(curr_pos[0]+n[0], curr_pos[1]+n[1]) for n in neighbours]
    ns = [n for n in ns if board[n] == '#']
    intsecs = [n for n in ns if n in intersections]
    ns = [n for n in ns if not n in visited]

    for intsec in intsecs:
        func = neighbours[dirs.index(direction)]
        if (curr_pos[0]+func[0], curr_pos[1]+func[1]) == intsec:
            ns = ns + [intsec]

    if len(ns) == 0:
        path.append(count)
        break

    elif len(ns) == 1:
        next_pos = ns[0]
        new_direction = directions[(next_pos[0]-curr_pos[0], next_pos[1]-curr_pos[1])]
        
        if new_direction != direction:
            path.append(count)
            path.append('R' if (dirs.index(new_direction)-dirs.index(direction))%4 == 1 else 'L')
            direction = new_direction
            count = 1

        else:
            count += 1

        curr_pos = next_pos
        visited.add(curr_pos)
        
    elif len(ns) == 3:
        intersections.add(curr_pos)
        
        count += 1
        
        func = neighbours[dirs.index(direction)]
        curr_pos = (curr_pos[0]+func[0], curr_pos[1]+func[1])
        visited.add(curr_pos)

# Print to find a manual solution to your problem
path = path[1:]

main_movement_routine, routine_a, routine_b, routine_c = [x for x in split_path(path)]
feed = ['n']

instr_dict[0] = 2 # Turn on program
new_robot = run(copy.deepcopy(instr_dict), inpt)

for item in [main_movement_routine, routine_a, routine_b, routine_c, feed]:
    tmp = ','.join(item) + '\n'
    tmp = [ord(x) for x in tmp]
    for val in tmp:
        inpt.append(val)

#output = ''
result_val = 0
while True:
    try:
        val = next(new_robot)
        #output += chr(val)
        result_val = val
    except:
        break

print(result_val)
