with open('input.txt') as f:
    instructions, network = f.read().split('\n\n')

network_dict = {}
network = network.split('\n')[:-1]

for transition in network:
    s_node, end_nodes = transition.split(' = ')
    end_nodes = end_nodes[1:-1].split(', ')
    network_dict[s_node] = {'L': end_nodes[0], 'R': end_nodes[1]}

i = 0
curr_node = 'AAA'
steps = 0
while curr_node != 'ZZZ':
    curr_node = network_dict[curr_node][instructions[i]]
    i = (i + 1) % len(instructions) 
    steps += 1

print(steps)
