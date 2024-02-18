def prog_run(a, num_instrs):
    curr_output = []

    registers = {
        'a': a,
        'b': 0,
        'c': 0,
        'd': 0,
    } 

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

        elif curr_instr.startswith('out'):
            _, x = curr_instr.split(' ')
            out_val = registers[x]
            curr_output.append(out_val)
            eip += 1

        tmp_1 = curr_output[:-1]
        tmp_2 = curr_output[1:]

        if any([tmp_1[i] == tmp_2[i] for i in range(len(tmp_1))]):
            return False
        else:
            if len(tmp_1) > 30:
                return True

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]
    num_instrs = len(instrs)

a = 0
found = False
while not found:
    if prog_run(a, num_instrs):
        print(a)
        found = True
    else:
        a += 1
