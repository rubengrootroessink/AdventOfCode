with open('input.txt', 'r') as f:
    instrs = [x.split('\n')[0] for x in f.readlines()]

clock_cycle = 0
register = 1
instruction_counter = 0
f_clock_cycle = True

CRT_row = []

while instruction_counter < len(instrs):
    clock_cycle += 1
    
    index = len(CRT_row)

    sprite = [register-1, register, register+1]
    if index in sprite:
        CRT_row.append('#')
    else:
        CRT_row.append('.')

    instr = instrs[instruction_counter]
    
    if instr == 'noop':
        instruction_counter += 1
    elif instr.startswith('addx'):
        if f_clock_cycle == True:
            f_clock_cycle = False
        else:
            _, number = instr.split(' ')
            register += int(number)
            instruction_counter += 1
            f_clock_cycle = True

    if len(CRT_row) % 40 == 0:
        print(''.join(CRT_row))
        CRT_row = []
