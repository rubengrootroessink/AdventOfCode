with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
}

num_instrs = len(instrs)

eip = 0

finished = False
while not finished:
    curr_instr = instrs[eip]

    if curr_instr.startswith('cpy'):
        _, x, y = curr_instr.split(' ')
        if x in ['a', 'b', 'c', 'd']:
            new_val = registers[x]
        else:
            new_val = int(x)
        registers[y] = new_val
        eip += 1
    elif curr_instr.startswith('inc'):
        _, x = curr_instr.split(' ')
        registers[x] += 1
        eip += 1
    elif curr_instr.startswith('dec'):
        _, x = curr_instr.split(' ')
        registers[x] -= 1
        eip += 1
    elif curr_instr.startswith('jnz'):
        _, x, y = curr_instr.split(' ')
        if x in ['a', 'b', 'c', 'd']:
            new_val = registers[x]
        else:
            new_val = int(x)

        if new_val != 0:
            nr_jumps = int(y)
            eip = eip + nr_jumps
        else:
            eip += 1

    if eip >= num_instrs:
        finished = True
        print(registers['a'])
