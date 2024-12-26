from itertools import permutations
import heapq

def resolve(mode, offset, instrs):
    if mode == 0:
        return instrs[instrs[offset]]
    else:
        return instrs[offset]

def run(instrs, inpt):
    eip = 0

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
                    instrs[instrs[eip+1]] = heapq.heappop(inpt)
                else:
                    instrs[eip+1] = heapq.heappop(inpt)
                    
            case 4:

                val_1 = resolve(mode_1, eip+1, instrs)
                output.append(val_1)

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

    return output

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = {}
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

max_val = 0
perms = permutations([0, 1, 2, 3, 4])
for perm in perms:
    inpt = [0]
    for amp in perm:
        output = run(instr_dict, [amp] + inpt)[-1]
        inpt = [output]

    max_val = max(output, max_val)

print(max_val)
