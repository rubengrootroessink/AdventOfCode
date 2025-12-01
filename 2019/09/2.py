from collections import defaultdict

class Computer:
    def __init__(self, program, input_data):
        self.program = program        
        self.eip = 0
        self.rel_base = 0
        self.input_list = input_data

    def parse_opcode(self, opcode):
        opcode = str(opcode).zfill(5)
        modes = [int(x) for x in opcode[0:3]][::-1]
        opcode = int(opcode[3:5])

        match opcode:
            case 1 | 2 | 7 | 8:
                return opcode, modes
            case 3 | 4 | 9:
                return opcode, modes[0:1]
            case 5 | 6:
                return opcode, modes[0:2]
            case 99:
                return opcode, []
    
    def reg_value(self, reg, mode, opcode, reg_num):
        match (mode, opcode, reg_num):
            case (0, _, _): return self.program[reg]
            case (1, _, _): return reg
            case (2, _, _): return self.program[reg] + self.rel_base

    # Opcode 1
    def add(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = self.program[reg_1] + self.program[reg_2]
        self.eip += 4

    # Opcode 2
    def mul(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = self.program[reg_1] * self.program[reg_2]
        self.eip += 4

    # Opcode 3
    def input(self, reg_1):
        self.program[reg_1] = self.input_list[0]
        self.eip += 2

    # Opcode 4
    def output(self, reg_1):
        print(self.program[reg_1])
        self.eip += 2

    # Opcode 5
    def jit(self, reg_1, reg_2):
        if self.program[reg_1] != 0: self.eip = self.program[reg_2]
        else: self.eip += 3

    # Opcode 6
    def jif(self, reg_1, reg_2):
        if self.program[reg_1] == 0: self.eip = self.program[reg_2]
        else: self.eip += 3

    # Opcode 7
    def lt(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(self.program[reg_1] < self.program[reg_2])
        self.eip += 4

    # Opcode 8
    def eq(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(self.program[reg_1] == self.program[reg_2])
        self.eip += 4

    # Opcode 9
    def adj_rel(self, reg_1):
        self.rel_base += self.program[reg_1]
        self.eip += 2

    def run(self):
        opcode, modes = self.parse_opcode(self.program[self.eip])
        while opcode != 99:
            regs = [self.reg_value(self.eip+1+i, modes[i], opcode, i) for i in range(len(modes))]

            match opcode:
                case 1: self.add(regs[0], regs[1], regs[2])
                case 2: self.mul(regs[0], regs[1], regs[2])
                case 3: self.input(regs[0])
                case 4: self.output(regs[0])
                case 5: self.jit(regs[0], regs[1])
                case 6: self.jif(regs[0], regs[1])
                case 7: self.lt(regs[0], regs[1], regs[2])
                case 8: self.eq(regs[0], regs[1], regs[2])
                case 9: self.adj_rel(regs[0])
        
            opcode, modes = self.parse_opcode(self.program[self.eip])

with open('input.txt') as f:
    data = [int(x) for x in f.read().strip().split(',')]

program = defaultdict(int)
for i, v in enumerate(data):
    program[i] = v

comp = Computer(program, [2])
comp.run()
