def run(instructions):
    accumulator = 0
    sp = 0
    
    indexes_visited = []
    
    found_loop = False
    while not found_loop:
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
    
    print(accumulator)

instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        data = data.split(' ')
        command = data[0]
        op = data[1][0]
        value = int(data[1][1:])
        instructions.append((command, op, value))

run(instructions)
