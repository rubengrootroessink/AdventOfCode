import math

def simulate(instructions):
    ship_hor, ship_ver = 0, 0
    way_hor, way_ver = 10, 1

    for instruction in instructions:
        instr, val = instruction
        
        if instr == 'F':
            ship_hor, ship_ver = ship_hor + val*way_hor, ship_ver + val*way_ver
        elif instr == 'E':
            way_hor += val
        elif instr == 'W':
            way_hor -= val
        elif instr == 'N':
            way_ver += val
        elif instr == 'S':
            way_ver -= val
        elif instr == 'L' or instr == 'R':
            degree = val
            radians = math.radians(degree)
            if instr == 'R':
                radians = -radians

            new_way_hor = round(way_hor * math.cos(radians) - way_ver * math.sin(radians))
            new_way_ver = round(way_hor * math.sin(radians) + way_ver * math.cos(radians))
            
            way_hor, way_ver = new_way_hor, new_way_ver
    return abs(ship_hor) + abs(ship_ver)

with open('input.txt', 'r') as file:
    instructions = []
    for i, line in enumerate(file.readlines()):
        data = line.split("\n")[0]
        instructions.append((data[0], int(data[1:])))

    print(simulate(instructions))
