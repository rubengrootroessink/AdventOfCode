input_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input_list.append(data)

hor_pos = sum([int(x[1]) for x in (x.split(' ') for x in input_list) if x[0] == 'forward'])
depth = sum([-int(x[1]) if x[0] == 'up' else int(x[1]) if x[0] == 'down' else 0 for x in (x.split(' ') for x in input_list)])

print(hor_pos * depth)
