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
    operations = f.read().split('\n\n\n\n')[0].split('\n\n')

total_count = 0
for op in operations:
    bf, op_code, af = parse_state(op)

    count = 0
    for name in names:
        executed = exec_op(name, op_code[1], op_code[2], op_code[3], bf)
        if executed == af:
            count += 1

    if count >= 3:
        total_count += 1

print(total_count)
