with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0].split(', ')
    
    faces = ['North', 'East', 'South', 'West']
    facing = 'North'
    hor, ver = 0, 0
    
    for instr in data:
        if instr[0] == 'L':
            facing = faces[(faces.index(facing) - 1) % 4]
        else:
            facing = faces[(faces.index(facing) + 1) % 4]
        if facing == 'North':
            ver += int(instr[1:])
        elif facing == 'South':
            ver -= int(instr[1:])
        elif facing == 'East':
            hor += int(instr[1:])    
        elif facing == 'West':
            hor -= int(instr[1:])

    print(abs(hor) + abs(ver))
