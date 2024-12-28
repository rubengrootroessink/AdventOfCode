# Inspired by others
from collections import defaultdict, deque
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

with open('input.txt') as f:
    instrs = [int(x) for x in f.read().strip().split(',')]

instr_dict = defaultdict(int)
for i, instr in enumerate(instrs):
    instr_dict[i] = instr

inpt = deque([])

robot = run(copy.deepcopy(instr_dict), inpt)

program = [
    "NOT C J",
    "AND D J",
    "AND H J",
    "NOT B T",
    "AND D T",
    "OR T J",
    "NOT A T",
    "OR T J",
    "RUN"
]

for line in program:
    for char in line:
        inpt.append(ord(char))
    inpt.append(10)

result_val = 0
#output = ""
while True:
    try:
        val = next(robot)
        #output += chr(val)
        result_val = val
    except Exception as e:
        break

print(result_val)
