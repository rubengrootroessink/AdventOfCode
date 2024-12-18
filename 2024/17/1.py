import math

with open('input.txt') as f:
    registers, instrs = f.read().strip().split('\n\n')

registers = [int(x.split(': ')[1]) for x in registers.split('\n')]
instrs = [int(x) for x in instrs.split(': ')[1].split(',')]

register_dict = {}
names = ['A', 'B', 'C']
for i, reg in enumerate(registers):
    register_dict[names[i]] = reg

num_instrs = len(instrs)
ip = 0

output_list = []

while True:

    if ip >= num_instrs: # In this case, the program halts
        break

    instr = instrs[ip]
    
    op = instrs[ip+1]
    if op in range(0, 4):
        combo_op = op
    elif op in range(4, 7):
        combo_op = register_dict[names[op-4]]
    elif op == 7:
        assert instr in [1, 3, 4] # Should never require a combo operand

    match instr:
        case 0 | 6 | 7: # adv, bdv or cdv
            num = register_dict['A']
            denom = 2**combo_op
            res = math.trunc(num / denom)

            if instr == 0:
                register_dict['A'] = res
            elif instr == 6:
                register_dict['B'] = res
            elif instr == 7:
                register_dict['C'] = res
            else:
                assert False # Should never occur

            ip += 2

        case 1 | 4: # bxl or bxc
            val_1 = register_dict['B']

            if instr == 1:
                val_2 = op
            else:
                val_2 = register_dict['C']
            
            register_dict['B'] = val_1 ^ val_2
            
            ip += 2

        case 2: # bst
            register_dict['B'] = combo_op % 8

            ip += 2

        case 3: # jnz
            if register_dict['A'] != 0:
                ip = op
            else:
                ip += 2

        case 5: # out
            output_list.append(combo_op % 8)

            ip += 2

print(','.join([str(x) for x in output_list]))
