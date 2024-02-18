with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

registers = {
    'a': 7,
    'b': 0,
    'c': 0,
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

        if y in ['a', 'b', 'c', 'd']: # Skips case where y is not a register (non-valid state)
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
            cmp_val = registers[x]
        else:
            cmp_val = int(x)

        if y in ['a', 'b', 'c', 'd']:
            jmp_val = registers[y]
        else:
            jmp_val = int(y)

        if cmp_val != 0:
            nr_jumps = jmp_val
            eip = eip + nr_jumps
        else:
            eip += 1

    elif curr_instr.startswith('tgl'):
        _, x = curr_instr.split(' ')
        if x in ['a', 'b', 'c', 'd']:
            new_val = registers[x]
        else:
            new_val = int(x)

        if eip+new_val in range(num_instrs):
            new_instr = instrs[eip+new_val]
            if new_instr.startswith('inc'):
                new_instr = new_instr.replace('inc', 'dec')
            elif new_instr.startswith('dec'):
                new_instr = new_instr.replace('dec', 'inc')
            elif new_instr.startswith('tgl'):
                new_instr = new_instr.replace('tgl', 'inc')
            elif new_instr.startswith('cpy'):
                new_instr = new_instr.replace('cpy', 'jnz')
            elif new_instr.startswith('jnz'):
                new_instr = new_instr.replace('jnz', 'cpy')

            instrs[eip+new_val] = new_instr
        eip += 1

    if eip >= num_instrs:
        finished = True
        print(registers['a'])
