import string

def dance(input_str):
    order = list(input_str)
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
    
    return ''.join(order)

with open('input.txt') as f:
    dance_steps = f.read().strip().split(',')

alphabet = string.ascii_lowercase
nr_programs = 16

result = alphabet[:nr_programs]

i = 0
seen = {result: i}

nr_rots = 1000000000
while nr_rots > 0:
    result = dance(result)
    i += 1
    
    if result in seen.keys():
        nr_rots = nr_rots % (i - seen[result])
    else:
        seen[result] = i
    
    nr_rots -= 1

print(result)
