with open('input.txt', 'r') as f:
    instrs = [x.split('\n')[0] for x in f.readlines()]

cycle_to_check = [20, 60, 100, 140, 180, 220]
result = []

clock_cycle = 0
register = 1
instruction_counter = 0
f_clock_cycle = True
while instruction_counter < len(instrs):
    clock_cycle += 1
    
    if clock_cycle in cycle_to_check:
        result.append(register*clock_cycle)

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
    
print(sum(result))
