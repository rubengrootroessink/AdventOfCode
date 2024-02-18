a, b = 1, 0

with open('input.txt', 'r') as f:
    instructions = []
    for line in f.readlines():
        instr = line.split('\n')[0]
        instruction = instr.split(' ')
        if ',' in instr:
            instruction = [x.split(',')[0] for x in instruction]
        instructions.append(instruction)

count = 0
found = False
while not found:
    instr = instructions[count]
    if instr[0] == 'hlf':
        globals()[instr[1]] //= 2
    elif instr[0] == 'tpl':
        globals()[instr[1]] *= 3
    elif instr[0] == 'inc':
        globals()[instr[1]] += 1
    elif instr[0] == 'jmp':
        count += int(instr[1])
    elif instr[0] == 'jie':
        if globals()[instr[1]] % 2 == 0:
            count += int(instr[2])
        else:
            count += 1
    elif instr[0] == 'jio':
        if globals()[instr[1]] == 1:
            count += int(instr[2])
        else:
            count += 1
    
    if instr[0] != 'jio' and instr[0] != 'jie' and instr[0] != 'jmp':
        count += 1
    
    if count >= len(instructions):
        found = True

print(b)
