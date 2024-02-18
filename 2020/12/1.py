def simulate(instructions):
    hor, ver = 0, 0
    face = 'E'
    
    clockwise = ['E', 'S', 'W', 'N']

    for instruction in instructions:
        instr, val = instruction
        
        if instr == 'F':
            if face == 'E':
                hor += val
            elif face == 'W':
                hor -= val
            elif face == 'N':
                ver += val
            elif face == 'S':
                ver -= val
        elif instr == 'E':
            hor += val
        elif instr == 'W':
            hor -= val
        elif instr == 'N':
            ver += val
        elif instr == 'S':
            ver -= val
        elif instr == 'L':
            turns = val // 90
            curr_index = clockwise.index(face)
            new_index = (curr_index - turns) % 4
            face = clockwise[new_index]
        elif instr == 'R':
            turns = val // 90
            curr_index = clockwise.index(face)
            new_index = (curr_index + turns) % 4
            face = clockwise[new_index]

    return abs(hor) + abs(ver)

with open('input.txt', 'r') as file:
    instructions = []
    for i, line in enumerate(file.readlines()):
        data = line.split("\n")[0]
        instructions.append((data[0], int(data[1:])))

    print(simulate(instructions))
