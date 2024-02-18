import copy

def exec_op(name, A, B, C, input_val):
    registers = copy.deepcopy(input_val)

    match name:

        # Addition
        case 'addr':
            registers[C] = registers[A] + registers[B]
        case 'addi':
            registers[C] = registers[A] + B

        # Multiplication
        case 'mulr':
            registers[C] = registers[A] * registers[B]
        case 'muli':
            registers[C] = registers[A] * B

        # Bitwise AND
        case 'banr':
            registers[C] = registers[A] & registers[B]
        case 'bani':
            registers[C] = registers[A] & B

        # Bitwise OR
        case 'borr':
            registers[C] = registers[A] | registers[B]
        case 'bori':
            registers[C] = registers[A] | B

        # Assignment
        case 'setr':
            registers[C] = registers[A]
        case 'seti':
            registers[C] = A

        # Greater-than
        case 'gtir':
            registers[C] = 1 if A > registers[B] else 0
        case 'gtri':
            registers[C] = 1 if registers[A] > B else 0
        case 'gtrr':
            registers[C] = 1 if registers[A] > registers[B] else 0

        # Equality
        case 'eqir':
            registers[C] = 1 if A == registers[B] else 0
        case 'eqri':
            registers[C] = 1 if registers[A] == B else 0
        case 'eqrr':
            registers[C] = 1 if registers[A] == registers[B] else 0
        case _:
            assert False

    return registers

def parse_state(state):
    bf, op, af = state.split('\n')
    bf = [int(x) for x in bf.split('[')[1].split(']')[0].split(', ')]
    op = [int(x) for x in op.split(' ')]
    af = [int(x) for x in af.split('[')[1].split(']')[0].split(', ')]
    return bf, op, af

names = ['addr', 'addi']
names += ['mulr', 'muli']
names += ['banr', 'bani']
names += ['borr', 'bori']
names += ['setr', 'seti']
names += ['gtir', 'gtri', 'gtrr']
names += ['eqir', 'eqri', 'eqrr']

with open('input.txt') as f:
    operations, prog = f.read().split('\n\n\n\n')
    operations = operations.split('\n\n')
    prog_instrs = [[int(y) for y in x.split(' ')] for x in prog[:-1].split('\n')]

instr_dict = {}

for op in operations:
    bf, op_code, af = parse_state(op)

    matching_instrs = []
    for name in [x for x in names if not x in instr_dict.values()]:
        executed = exec_op(name, op_code[1], op_code[2], op_code[3], bf)
        if executed == af:
            matching_instrs.append(name)

    if len(matching_instrs) == 1:
        instr_dict[op_code[0]] = matching_instrs[0]

registers = [0, 0, 0, 0]
for instr in prog_instrs:
    registers = exec_op(instr_dict[instr[0]], instr[1], instr[2], instr[3], registers)

print(registers[0])
