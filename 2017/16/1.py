import string

with open('input.txt') as f:
    dance_steps = f.read().strip().split(',')

alphabet = string.ascii_lowercase
nr_programs = 16

order = list(alphabet[:nr_programs])

for step in dance_steps:
    if step.startswith('s'):
        nr_spins = int(step[1:])
        order = order[-nr_spins:] + order[:-nr_spins]
    elif step.startswith('x'):
        a, b = [int(x) for x in step[1:].split('/')]
        a_val, b_val = order[a], order[b]
        order[a] = b_val
        order[b] = a_val
    elif step.startswith('p'):
        a, b = step[1:].split('/')
        a_index, b_index = order.index(a), order.index(b)
        order[a_index] = b
        order[b_index] = a

print(''.join(order))
