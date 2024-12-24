from itertools import combinations

dependency_dict = {}
start_wires = {}

with open('input.txt') as f:
    start_wires, gates = f.read().strip().split('\n\n')

start_wires = [x.strip().split(': ') for x in start_wires.split('\n')]
start_wires = {x[0]: int(x[1]) for x in start_wires}

gates = [x.strip().split(' ') for x in gates.split('\n')]
gates = [(x[0], x[1], x[2], x[4]) for x in gates]

output_vals = []
for gate in gates:
    input_1, op, input_2, output = gate
    dependency_dict[output] = (input_1, op, input_2)
    if output.startswith('z'):
        output_vals.append(output)

z_vals = [z for z in sorted(dependency_dict.keys(), reverse=True) if z.startswith('z')]

result = []

for i in range(0, len(z_vals)-1):
    prev_nr_string = '0'*(2-len(str(i-1))) + str(i-1)
    nr_string = '0'*(2-len(str(i))) + str(i)
    z_val = 'z' + nr_string

    input_1, op, input_2 = dependency_dict[z_val]

    if i == 0: # Special case (half adder at the start), we assume no crossed wires for simplicity
        assert input_1 == 'x00'
        assert input_2 == 'y00'
        assert op == 'XOR'
    elif i == 1: # Special case (limited dependencies), we assume no crossed wires for simplicity
        assert op == 'XOR'
        a_1, a_op, a_2 = dependency_dict[input_1]
        b_1, b_op, b_2 = dependency_dict[input_2]

        assert {a_op, b_op} == {'XOR', 'AND'}

        if a_op != 'AND':
            tmp = (b_1, b_op, b_2)
            b_1, b_op, b_2 = a_1, a_op, a_2
            a_1, a_op, a_2 = tmp

        a_1, a_2 = list(sorted([a_1, a_2]))
        b_1, b_2 = list(sorted([b_1, b_2]))

        assert a_op == 'AND'
        assert a_1 == 'x' + prev_nr_string
        assert a_2 == 'y' + prev_nr_string

        assert b_op == 'XOR'
        assert b_1 == 'x' + nr_string
        assert b_2 == 'y' + nr_string
    else: 
        
        if op != 'XOR':
            result.append(z_val)
            continue

        a_1, a_op, a_2 = dependency_dict[input_1]
        b_1, b_op, b_2 = dependency_dict[input_2]
         
        if {a_op, b_op} != {'OR', 'XOR'}:
            if (a_op == 'XOR' and b_op != 'OR') or (a_op == 'OR' and b_op != 'XOR'):
                result.append(input_2)
            elif (a_op != 'XOR' and b_op == 'OR') or (a_op != 'OR' and b_op == 'XOR'):
                result.append(input_1)
            continue

        if a_op != 'XOR':
            tmp = (b_1, b_op, b_2)
            b_1, b_op, b_2 = a_1, a_op, a_2
            a_1, a_op, a_2 = tmp

        a_1, a_2 = list(sorted([a_1, a_2]))
        b_1, b_2 = list(sorted([b_1, b_2]))

        assert a_op == 'XOR'
        assert b_op == 'OR'
        
        if a_1 != 'x' + nr_string:
            continue
        if a_2 != 'y' + nr_string:
            continue
        
        c_1, c_op, c_2 = dependency_dict[b_1]
        d_1, d_op, d_2 = dependency_dict[b_2]

        if {c_op, d_op} != {'AND', 'AND'}:
            if c_op != 'AND':
                result.append(b_1)
            elif d_op != 'AND':
                result.append(b_2)
            elif c_op != 'AND' and d_op != 'AND':
                assert False
            continue

        if {c_1, c_2} != {'x' + prev_nr_string, 'y' + prev_nr_string}:
            tmp = (d_1, d_op, d_2)
            d_1, d_op, d_2 = c_1, c_op, c_2
            c_1, c_op, c_2 = tmp
        
        c_1, c_2 = list(sorted([c_1, c_2]))
        d_1, d_2 = list(sorted([d_1, d_2]))

        assert c_op == 'AND'
        assert d_op == 'AND'
       
        if c_1 != 'x' + prev_nr_string:
            continue
        if c_2 != 'y' + prev_nr_string:
            continue

print(','.join(list(sorted(result))))
