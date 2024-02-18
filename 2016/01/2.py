with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0].split(', ')
    
    faces = ['North', 'East', 'South', 'West']
    
    face_vars = {
        'North': ['ver', '+'],
        'South': ['ver', '-'],
        'East': ['hor', '+'],
        'West': ['hor', '-']
    }
    
    facing = 'North'
    hor, ver = 0, 0
    
    visited = set()
    
    for instr in data:
        if instr[0] == 'L':
            facing = faces[(faces.index(facing) - 1) % 4]
        else:
            facing = faces[(faces.index(facing) + 1) % 4]
        
        line = int(instr[1:])
        for _ in range(line):
            globals()[face_vars[facing][0]] += int(face_vars[facing][1] + str(1))
            if (hor, ver) in visited:
                print(abs(hor) + abs(ver))
                exit()
            else:
                visited.add((hor, ver))
