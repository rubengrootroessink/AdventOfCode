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
            case 1 | 2:

                val_1 = resolve(mode_1, eip+1, instrs)
                val_2 = resolve(mode_2, eip+2, instrs)

                res = 0
                
                if op_code == 1:
                    res = val_1 + val_2
                elif op_code == 2:
                    res = val_1 * val_2
                
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

            case 99:

                finished = True

        eip += eip_jumps

    return output

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = {}
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

outputs = run(instr_dict, [1])
print(outputs[-1])
