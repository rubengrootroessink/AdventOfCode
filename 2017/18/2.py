import copy
from collections import defaultdict, deque

def parse_instr(instr):
    p_instr = instr.split(' ')
    if p_instr[1].isdigit() or p_instr[1].startswith('-'):
        p_instr[1] = int(p_instr[1])
    if len(p_instr) == 3:
        if p_instr[2].isdigit() or p_instr[2].startswith('-'):
            p_instr[2] = int(p_instr[2])

    if p_instr[0]:
        return tuple(p_instr)

queue_dict = {
    0: deque([]),
    1: deque([])
}

with open('input.txt') as f:
    instrs = [parse_instr(x.strip()) for x in f.readlines()]

nr_instrs = len(instrs)

finished = {
    0: False,
    1: False
}

class Program:
    def __init__(self, ID, regs, eip):
        self.ID = ID
        self.regs = regs
        self.eip = eip
        self.regs['p'] = self.ID
        self.count = 0

    def next(self):
        
        if not self.eip in range(nr_instrs):
            finished[self.ID] = True
            return False

        instr = instrs[self.eip]
        name = instr[0]
        
        if name == 'snd':
            freq = instr[1]
            freq = freq if type(freq) == int else self.regs[freq]
            queue_dict[0 if self.ID == 1 else 1].append(freq)
            self.eip += 1
            self.count += 1
        
        elif name == 'set':
            reg, val = instr[1:]
            self.regs[reg] = val if type(val) == int else self.regs[val]
            self.eip += 1
        
        elif name == 'add':
            reg, val = instr[1:]
            self.regs[reg] += val if type(val) == int else self.regs[val]
            self.eip += 1

        elif name == 'mul':
            reg, val = instr[1:]
            self.regs[reg] *= val if type(val) == int else self.regs[val]
            self.eip += 1

        elif name == 'mod':
            reg, val = instr[1:]
            self.regs[reg] = self.regs[reg] % (val if type(val) == int else self.regs[val])
            self.eip += 1
    
        elif name == 'rcv':

            if len(queue_dict[self.ID]) > 0:
                self.regs[instr[1]] = queue_dict[self.ID].popleft()
                self.eip += 1
            else:
                return False
            
        elif name == 'jgz':
            x, y = instr[1:]
            x = x if type(x) == int else self.regs[x]
            y = y if type(y) == int else self.regs[y]
        
            if x > 0:
                self.eip += y
            else:
                self.eip += 1

        return True

regs = copy.deepcopy(defaultdict(int))
eip = 0

zero = Program(0, copy.deepcopy(regs), eip)
one = Program(1, copy.deepcopy(regs), eip)

while not finished[0] and not finished[1]:
    zero.next()
    one.next()
    
    # Deadlock
    if len(queue_dict[0]) == 0 == len(queue_dict[1]) and not zero.next() and not one.next():
        finished[0] = True
        finished[1] = True

print(one.count)
