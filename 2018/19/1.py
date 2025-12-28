class VM:
    regs = {}

    def __init__(self, regs, eip_reg, program):
        for i, reg_val in enumerate(regs):
            self.regs[i] = reg_val
        self.program = program
        self.eip = 0
        self.eip_reg = eip_reg

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

    def run(self):
        while self.eip in range(len(self.program)):
            self.regs[self.eip_reg] = self.eip
            opcode, A, B, C = self.program[self.eip]
            self.exec_instr(opcode, A, B, C)
            self.eip = self.regs[self.eip_reg] + 1

with open('input.txt') as f:
    instrs = [x.strip().split(' ') for x in f.readlines()]
    eip_reg = int(instrs[0][1])
    instrs = [(x[0], int(x[1]), int(x[2]), int(x[3])) for x in instrs[1:]]

vm = VM([0]*6, eip_reg, instrs)
vm.run()
print(vm.get_regs()[0])
