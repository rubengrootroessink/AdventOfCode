def resolve(output, dependency_dict, start_vals):
    if output in start_vals.keys():
        return start_vals[output]

    else:
        v = dependency_dict[output]
        input_1 = v[1]
        op = v['op']
        input_2 = v[2]
        
        res_1 = resolve(input_1, dependency_dict, start_vals)
        res_2 = resolve(input_2, dependency_dict, start_vals)

        match op:
            case 'XOR':
                return res_1 ^ res_2
            case 'OR':
                return res_1 | res_2
            case 'AND':
                return res_1 & res_2

with open('input.txt') as f:
    start_wires, gates = f.read().strip().split('\n\n')

start_wires = [x.strip().split(': ') for x in start_wires.split('\n')]
start_wires = {x[0]: int(x[1]) for x in start_wires}

gates = [x.strip().split(' ') for x in gates.split('\n')]
gates = [(x[0], x[1], x[2], x[4]) for x in gates]

dependency_dict = {}
output_vals = []
for gate in gates:
    input_1, op, input_2, output = gate
    dependency_dict[output] = {1: input_1, 'op': op, 2: input_2}
    if output.startswith('z'):
        output_vals.append(output)

final_num = []
for o in sorted(output_vals, reverse=True):
    final_num.append(resolve(o, dependency_dict, start_wires))

print(int(''.join([str(x) for x in final_num]), 2))
