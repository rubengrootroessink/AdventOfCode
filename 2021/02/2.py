input_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input_list.append(data)

hor_pos, aim, depth = 0, 0, 0
[(hor_pos := hor_pos + int(val), depth := depth + (aim * int(val))) if command == 'forward' else (aim := aim - int(val)) if command == 'up' else (aim := aim + int(val)) for command, val in (x.split(' ') for x in input_list)]

print(hor_pos * depth)
