from collections import defaultdict

def parse_instr(instr):
    p_instr = instr.split(' ')
    if p_instr[1].isdigit() or p_instr[1].startswith('-'):
        p_instr[1] = int(p_instr[1])
    if len(p_instr) == 3:
        if p_instr[2].isdigit() or p_instr[2].startswith('-'):
            p_instr[2] = int(p_instr[2])

    if p_instr[0]:
        return tuple(p_instr)

with open('input.txt') as f:
    instrs = [parse_instr(x.strip()) for x in f.readlines()]

len_instrs = len(instrs)

regs = defaultdict(int)

eip = 0

sounds = []
while eip in range(len_instrs):
    instr = instrs[eip]
    name = instr[0]
    if name == 'snd':
        freq = instr[1]
        freq = freq if type(freq) == int else regs[freq]
        sounds.append(freq)
        eip += 1
    elif name == 'set':
        reg, val = instr[1:]
        regs[reg] = val if type(val) == int else regs[val]
        eip += 1
    elif name == 'add':
        reg, val = instr[1:]
        regs[reg] += val if type(val) == int else regs[val]
        eip += 1
    elif name == 'mul':
        reg, val = instr[1:]
        regs[reg] *= val if type(val) == int else regs[val]
        eip += 1
    elif name == 'mod':
        reg, val = instr[1:]
        regs[reg] = regs[reg] % (val if type(val) == int else regs[val])
        eip += 1
    elif name == 'rcv':
        rec_val = instr[1]
        rec_val = rec_val if type(rec_val) == int else regs[rec_val]
        if rec_val != 0:
            prev_sound = sounds[-1]
            print(prev_sound)
            break
        eip += 1
    elif name == 'jgz':
        x, y = instr[1:]
        x = x if type(x) == int else regs[x]
        y = y if type(y) == int else regs[y]
        
        if x > 0:
            eip += y
        else:
            eip += 1
