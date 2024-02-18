def runs_full(instructions):
    accumulator = 0
    sp = 0
    
    indexes_visited = []
    
    found_loop = False
    while not found_loop:
        if sp >= len(instructions):
            return (True, accumulator)

        command = instructions[sp]
        if command[0] == 'nop':
            sp += 1
            if sp in indexes_visited:
                found_loop = True
                break
        elif command[0] == 'acc':
            sp += 1
            if sp in indexes_visited:
                found_loop = True
                break
            if command[1] == '-':
                accumulator -= command[2]
            elif command[1] == '+':
                accumulator += command[2]
        elif command[0] == 'jmp':
            if command[1] == '-':
                sp -= command[2]
            elif command[1] == '+':
                sp += command[2]
            if sp in indexes_visited:
                found_loop = True
                break
        indexes_visited.append(sp)
    
    return (not found_loop, 0)

instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        data = data.split(' ')
        command = data[0]
        op = data[1][0]
        value = int(data[1][1:])
        instructions.append((command, op, value))
        
for i, instruction in enumerate(instructions):
    new_instructions = instructions.copy()
    if instruction[0] == 'nop':
        new_instructions[i] = ('jmp', instruction[1], instruction[2])
    elif instruction[0] == 'jmp':
        new_instructions[i] = ('nop', instruction[1], instruction[2])
    result = runs_full(new_instructions)
    if result[0]:
        print(result[1])
        break
