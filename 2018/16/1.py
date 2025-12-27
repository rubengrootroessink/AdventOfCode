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

opcodes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

total_count = 0
for c in checks:
    b, i, a = c.split('\n')
    b = [int(x) for x in b.split('Before: [')[1][:-1].split(', ')]
    i = [int(x) for x in i.split(' ')]
    a = [int(x) for x in a.split('After:  [')[1][:-1].split(', ')]

    count = 0
    for opcode in opcodes:
        vm = VM(b)
        vm.exec_instr(opcode, i[1], i[2], i[3])

        if a == vm.get_regs():
            count += 1

    if count >= 3:
        total_count += 1

print(total_count)
