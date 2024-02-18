with open('input.txt') as f:
    instrs = [x.split('\n')[0].split(' ') for x in f.readlines()]

length = 0
pos = (0,0)
boundaries = []

for instr in instrs:
    direction, number, color = instr
    direction = ['R', 'D', 'L', 'U'][int(color[7])]
    number = int(color[2:7], 16)

    if direction == 'R':
        pos = (pos[0] + number, pos[1])
    elif direction == 'L':
        pos = (pos[0] - number, pos[1])
    elif direction == 'D':
        pos = (pos[0], pos[1] + number)
    elif direction == 'U':
        pos = (pos[0], pos[1] - number)

    length += number
    boundaries.append(pos)

# Trapezoid formula (shoelace formula)
trapezoids = list(zip(boundaries, boundaries[1:] + [boundaries[0]]))
area = int(0.5*sum([(a[1]+b[1])*(a[0]-b[0]) for a,b in trapezoids]))

# Pick's Theorem
print(int(area) + length // 2 + 1)
