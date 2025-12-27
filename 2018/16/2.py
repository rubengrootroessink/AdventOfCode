class VM:
    regs = {}

    def __init__(self, regs):
        for i, reg_val in enumerate(regs):
            self.regs[i] = reg_val

    def exec_instr(self, opcode, A, B, C):
        match opcode:
            case 'addr': self.regs[C] = self.regs[A] + self.regs[B]
            case 'addi': self.regs[C] = self.regs[A] + B
            case 'mulr': self.regs[C] = self.regs[A] * self.regs[B]
            case 'muli': self.regs[C] = self.regs[A] * B
            case 'banr': self.regs[C] = self.regs[A] & self.regs[B]
            case 'bani': self.regs[C] = self.regs[A] & B
            case 'borr': self.regs[C] = self.regs[A] | self.regs[B]
            case 'bori': self.regs[C] = self.regs[A] | B
            case 'setr': self.regs[C] = self.regs[A]
            case 'seti': self.regs[C] = A
            case 'gtir': self.regs[C] = int(A > self.regs[B])
            case 'gtri': self.regs[C] = int(self.regs[A] > B)
            case 'gtrr': self.regs[C] = int(self.regs[A] > self.regs[B])
            case 'eqir': self.regs[C] = int(A == self.regs[B])
            case 'eqri': self.regs[C] = int(self.regs[A] == B)
            case 'eqrr': self.regs[C] = int(self.regs[A] == self.regs[B])

    def get_regs(self):
        res = []
        for i in range(len(self.regs)):
            res.append(self.regs[i])
        return res

with open('input.txt') as f:
    checks, instrs = f.read().strip().split('\n\n\n\n')
    checks = checks.split('\n\n')
    instrs = [[int(x) for x in y.split(' ')] for y in instrs.split('\n')]

opcode_dict = {
    'addr': set(),
    'addi': set(),
    'mulr': set(),
    'muli': set(),
    'banr': set(),
    'bani': set(),
    'borr': set(),
    'bori': set(),
    'setr': set(),
    'seti': set(),
    'gtir': set(),
    'gtri': set(),
    'gtrr': set(),
    'eqir': set(),
    'eqri': set(),
    'eqrr': set()
}

for c in checks:
    b, i, a = c.split('\n')
    b = [int(x) for x in b.split('Before: [')[1][:-1].split(', ')]
    i = [int(x) for x in i.split(' ')]
    a = [int(x) for x in a.split('After:  [')[1][:-1].split(', ')]

    for opcode in opcode_dict.keys():
        vm = VM(b)
        vm.exec_instr(opcode, i[1], i[2], i[3])

        if a == vm.get_regs():
            opcode_dict[opcode].add(i[0])

rev_opcode_dict = {}

while any(type(x) != int for x in opcode_dict.values()):
    tuples = opcode_dict.items()
    for k, v in tuples:
        if type(v) == int:
            continue
        
        non_assigned_values = v - set(rev_opcode_dict.keys())

        if len(non_assigned_values) == 1:
            value = list(non_assigned_values)[0]
            opcode_dict[k] = value
            rev_opcode_dict[value] = k

vm = VM([0]*4)
for instr in instrs:
    opcode, A, B, C = instr
    opcode = rev_opcode_dict[opcode]
    vm.exec_instr(opcode, A, B, C)

print(vm.get_regs()[0])
