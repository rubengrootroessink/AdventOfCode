def compare(lhs, op, rhs):
    if op == '==':
        return lhs == rhs
    elif op == '<=':
        return lhs <= rhs
    elif op == '>=':
        return lhs >= rhs
    elif op == '<':
        return lhs < rhs
    elif op == '>':
        return lhs > rhs
    elif op == '!=':
        return lhs != rhs

with open('input.txt') as f:
    instrs = [x.split('\n')[0] for x in f.readlines()]

registers = {}

max_val = 0

for instr in instrs:
    reg, op, num, _, cond = instr.split(' ', 4)

    if not reg in registers.keys():
        registers[reg] = 0
    
    num = int(num)
    
    lhs, comp, rhs = cond.split(' ')
    lhs = int(lhs) if lhs.lstrip('-').isdigit() else 0 if not lhs in registers.keys() else registers[lhs]
    rhs = int(rhs) if rhs.lstrip('-').isdigit() else 0 if not rhs in registers.keys() else registers[rhs]
    
    if compare(lhs, comp, rhs):
        if op == 'inc':
            registers[reg] += num
        elif op == 'dec':
            registers[reg] -= num

    max_val = max(max_val, max(registers.values()))

print(max_val)
