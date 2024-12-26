from itertools import permutations
import heapq
import copy

def resolve(mode, offset, instrs):
    if mode == 0:
        return instrs[instrs[offset]]
    else:
        return instrs[offset]

inputs = {}

def run(instrs, char):
    eip = 0

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

                val_1 = resolve(mode_1, eip+1, instrs)
                val_2 = resolve(mode_2, eip+2, instrs)

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
                else:
                    instrs[eip+3] = res
                
                eip_jumps += 2

            case 3:
                
                if mode_1 == 0:
                    instrs[instrs[eip+1]] = heapq.heappop(inputs[char])
                else:
                    instrs[eip+1] = heapq.heappop(inputs[char])
                    
            case 4:

                val_1 = resolve(mode_1, eip+1, instrs)
                yield val_1

            case 5 | 6:
                
                val_1 = resolve(mode_1, eip+1, instrs)
                val_2 = resolve(mode_2, eip+2, instrs)

                if op_code == 5 and val_1 != 0:
                    eip = val_2
                    eip_jumps = 0
                elif op_code == 6 and val_1 == 0:
                    eip = val_2
                    eip_jumps = 0
                else:
                    eip_jumps += 1

            case 99:

                finished = True

        eip += eip_jumps

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = {}
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

max_val = 0
perms = permutations([5, 6, 7, 8, 9])
for perm in perms:

    inputs['A'] = [perm[0]] + [0]
    inputs['B'] = [perm[1]]
    inputs['C'] = [perm[2]]
    inputs['D'] = [perm[3]]
    inputs['E'] = [perm[4]]

    a = run(copy.deepcopy(instr_dict), 'A')
    b = run(copy.deepcopy(instr_dict), 'B')
    c = run(copy.deepcopy(instr_dict), 'C')
    d = run(copy.deepcopy(instr_dict), 'D')
    e = run(copy.deepcopy(instr_dict), 'E')

    while True:
        try:
            inputs['B'].append(next(a))
            inputs['C'].append(next(b))
            inputs['D'].append(next(c))
            inputs['E'].append(next(d))
            inputs['A'].append(next(e))
        except:
            break

    max_val = max(inputs['A'][-1], max_val)

print(max_val)
