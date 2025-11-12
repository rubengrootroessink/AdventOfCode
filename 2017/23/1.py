from collections import defaultdict

registers = defaultdict(int)

def get_val(x):
    try:
        return int(x)
    except:
        return registers[x]

with open('input.txt') as f:
    instrs = [tuple(x.strip().split(' ')) for x in f.readlines()]

num_instrs = len(instrs)

count = 0

eip = 0
while eip in range(num_instrs):
    instr = instrs[eip]

    if instr[0] == 'set':
        registers[instr[1]] = get_val(instr[2])
    elif instr[0] == 'sub':
        registers[instr[1]] -= get_val(instr[2])
    elif instr[0] == 'mul':
        registers[instr[1]] *= get_val(instr[2])
        count += 1
    elif instr[0] == 'jnz':
        if get_val(instr[1]) != 0:
            eip += (get_val(instr[2]) - 1)
    eip += 1

print(count)
