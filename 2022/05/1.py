with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

start_stack = data[0].split('\n')
instrs = [x for x in data[1].split('\n') if x != '']

stack_data, nr_stacks = start_stack[:-1], start_stack[-1]
nr_stacks = int([x for x in nr_stacks.split(' ') if x != ''][-1])

stack = []
for i in range(nr_stacks):
    stack.append([])

n = 4
for line in stack_data[::-1]:
    values = [(line[i:i+n]) for i in range(0, len(line), n)]
    values = [x[:3] if len(x) == 4 else x for x in values]
    for i, value in enumerate(values):
        if value != '   ':
            stack[i].append(value[1])

for instr in instrs:
    values = instr.split(' ')
    values = [int(x) for x in [values[1]] + [values[3]] + [values[5]]]
    for i in range(values[0]):
        tmp_val = stack[values[1]-1][-1]
        stack[values[1]-1].pop()
        stack[values[2]-1].append(tmp_val)

result = ''
for item in stack:
    result += item[-1]

print(result)
