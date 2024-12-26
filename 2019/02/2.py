import copy

def run(instrs, pos_1, pos_2):
    eip = 0
    instrs[1] = pos_1
    instrs[2] = pos_2
    
    finished = False
    while not finished:
        op_code = instrs[eip]

        match op_code:
            case 1 | 2:
                val_1 = instrs[instrs[eip+1]]
                val_2 = instrs[instrs[eip+2]]
                res = 0
                if op_code == 1:
                    res = val_1 + val_2
                elif op_code == 2:
                    res = val_1 * val_2
                instrs[instrs[eip+3]] = res
                eip += 4
            case 99:
                finished = True

    return instrs

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = {}
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

result_dict = run(copy.deepcopy(instr_dict), 12, 2)

found = False
for noun in range(0, 100):
    for verb in range(0, 100):
        result_dict = run(copy.deepcopy(instr_dict), noun, verb)
        if result_dict[0] == 19690720:
            print(noun*100+verb)
            found = True
            break

    if found:
        break
