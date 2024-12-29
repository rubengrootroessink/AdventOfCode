from collections import defaultdict
from itertools import permutations
import heapq
import copy

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

loc_dict = defaultdict(int)

curr_pos = (0, 0)
queue = [(curr_pos, [], 0)]
visited = {curr_pos}

locs = defaultdict(str)
locs[curr_pos] = '.'

neighbour_dict = {
    'n': (lambda x: (x[0], x[1]-1), 1, 2),
    's': (lambda x: (x[0], x[1]+1), 2, 1),
    'w': (lambda x: (x[0]-1, x[1]), 3, 4),
    'e': (lambda x: (x[0]+1, x[1]), 4, 3)
}

found = False
while queue:

    robot = run(copy.deepcopy(instr_dict))
    
    node, path, weight = heapq.heappop(queue)

    for item in path:
        func, instr, back_instr = neighbour_dict[item]
        inpt.append(instr)
        status = next(robot)

    for i in ['n', 's', 'w', 'e']:
        func, instr, back_instr = neighbour_dict[i]

        inpt.append(instr)
        status = next(robot)
        
        new_node = func(node)
        if status == 0:
            locs[new_node] = '#'
            visited.add(new_node)
        elif status == 1:
            locs[new_node] = '.'
            if not new_node in visited:
                heapq.heappush(queue, (new_node, path + [i], weight + 1))
                visited.add(new_node)
            inpt.append(back_instr)
            status = next(robot)
        if status == 2:
            locs[new_node] = 'O'

minutes = 0
while '.' in locs.values():
    o_elems = [k for k, v in locs.items() if v == 'O']
    for o in o_elems:
        ns = [neighbour_dict[d][0](o) for d in ['n', 's', 'w', 'e']]
        for n in ns:
            if locs[n] == '.':
                locs[n] = 'O'

    minutes += 1

print(minutes)