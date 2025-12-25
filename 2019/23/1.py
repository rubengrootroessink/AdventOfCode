# Inspired by others
from collections import deque, defaultdict
import copy

class Computer:
    def __init__(self, program, ip):
        self.program = program        
        self.eip = 0
        self.rel_base = 0
        self.ip = ip
        self.input_list = deque()
        self.input_list.append(ip)
        self.output_list = deque()

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
            case (2, 3, 0): return reg + self.rel_base
            case (_, 3, 0): return reg
            case (0, _, 0): return self.program[reg]
            case (2, _, 2): return reg + self.rel_base
            case (_, _, 2): return reg
            case (0, _, _): return self.program[reg]
            case (1, _, _): return reg
            case (2, _, _): return self.program[reg + self.rel_base]

    # Opcode 1
    def add(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = reg_1 + reg_2
        self.eip += 4

    # Opcode 2
    def mul(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = reg_1 * reg_2
        self.eip += 4

    # Opcode 3
    def input(self, reg_1):
        if len(self.input_list) > 0:
            self.program[reg_1] = self.input_list.popleft()
            self.eip += 2
        else:
            self.program[reg_1] = -1
            self.eip += 2
            return (-1, -1, -1)

    # Opcode 4
    def output(self, reg_1):
        self.output_list.append(reg_1)
        if len(self.output_list) >= 3:
            addr = self.output_list.popleft()
            x = self.output_list.popleft()
            y = self.output_list.popleft()
            self.eip += 2
            return (addr, x, y)
        else:
            self.eip += 2

    # Opcode 5
    def jit(self, reg_1, reg_2):
        if reg_1 != 0: self.eip = reg_2
        else: self.eip += 3

    # Opcode 6
    def jif(self, reg_1, reg_2):
        if reg_1 == 0: self.eip = reg_2
        else: self.eip += 3

    # Opcode 7
    def lt(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(reg_1 < reg_2)
        self.eip += 4

    # Opcode 8
    def eq(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(reg_1 == reg_2)
        self.eip += 4

    # Opcode 9
    def adj_rel(self, reg_1):
        self.rel_base += reg_1
        self.eip += 2

    def run(self): 
        opcode, modes = self.parse_opcode(self.program[self.eip])
        while True:
            
            regs = [self.reg_value(self.program[self.eip+1+i], modes[i], opcode, i) for i in range(len(modes))]
            
            match opcode:
                case 1: self.add(regs[0], regs[1], regs[2])
                case 2: self.mul(regs[0], regs[1], regs[2])
                case 3:
                    res = self.input(regs[0])
                    if res:
                        return res
                case 4:
                    res = self.output(regs[0])
                    if res:
                        return res
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

comps = [Computer(copy.deepcopy(program), i) for i in range(50)]

i = 0

while True:
    (addr, x, y) = comps[i].run()

    if addr != -1 and addr != 255:
        comps[addr].input_list.append(x)
        comps[addr].input_list.append(y)
        i = addr

    elif addr == 255:
        print(y)
        break

    else:
        i = (i + 1) % 50
