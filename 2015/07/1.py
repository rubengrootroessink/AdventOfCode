def calc_op(x, y, op):
    if op == 'AND':
        return x & y
    elif op == 'OR':
        return x | y
    elif op == 'LSHIFT':
        return x << y
    elif op == 'RSHIFT':
        return x >> y

wires = {}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.split('\n')[0].split(' ') for line in lines]

    to_evaluate = []
    while len(lines) != 0:
        for line in lines:
            if len(line) == 3:
                if line[0].isdigit():
                    wires[line[2]] = int(line[0])
                elif line[0] in wires.keys():
                    wires[line[2]] = wires[line[0]]
                else:
                    to_evaluate.append(line)
            if len(line) == 4:
                if line[1].isdigit():
                    wires[line[3]] = ~int(line[1])
                elif line[1] in wires.keys():
                    wires[line[3]] = ~wires[line[1]]
                else:
                    to_evaluate.append(line)
            if len(line) == 5:
                if line[0].isdigit() and line[2].isdigit():
                    wires[line[4]] = calc_op(int(line[0]), int(line[2]), line[1])
                elif line[0] in wires.keys() and line[2].isdigit():
                    wires[line[4]] = calc_op(wires[line[0]], int(line[2]), line[1])
                elif line[0].isdigit() and line[2] in wires.keys():
                    wires[line[4]] = calc_op(int(line[0]), wires[line[2]], line[1])
                elif line[0] in wires.keys() and line[2] in wires.keys():
                    wires[line[4]] = calc_op(wires[line[0]], wires[line[2]], line[1])
                else:
                    to_evaluate.append(line)
         
        lines = to_evaluate
        to_evaluate = []

print(wires['a'])
