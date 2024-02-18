from functools import reduce

def lcm(x,y):
    tmp = x
    while (tmp % y) != 0:
        tmp += x
    return tmp

with open('input.txt') as f:
    instructions, network = f.read().split('\n\n')

network_dict = {}
network = network.split('\n')[:-1]

for transition in network:
    s_node, end_nodes = transition.split(' = ')
    end_nodes = end_nodes[1:-1].split(', ')
    network_dict[s_node] = {'L': end_nodes[0], 'R': end_nodes[1]}

start_nodes = [x for x in network_dict.keys() if x.endswith('A')]
network_traversal = {s: [s] for s in start_nodes}

i = 0
while not all([x[-1].endswith('Z') for x in network_traversal.values()]):
    for s, v in network_traversal.items():
        if v[-1].endswith('Z'):
            continue
        else:
            next_node = network_dict[v[-1]][instructions[i]]
            network_traversal[s].append(next_node)
    i = (i + 1) % len(instructions)

print(reduce(lcm, [len(x)-1 for x in network_traversal.values()]))
