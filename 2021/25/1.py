def step(input_dict, max_x, max_y):
    temp_dict = {}
    for (x,y), value in input_dict.items():
        if value == '>':
            if ((x+1)%max_x,y) in input_dict.keys():
                temp_dict[(x,y)] = value
            else:
                temp_dict[((x+1)%max_x, y)] = value
        else:
            temp_dict[(x,y)] = value

    result_dict = {}
    for (x,y), value in temp_dict.items():
        if value == 'v':
            if (x,(y+1)%max_y) in temp_dict.keys():
                result_dict[(x,y)] = value
            else:
                result_dict[(x,(y+1)%max_y)] = value
        else:
            result_dict[(x,y)] = value
    return result_dict

def print_dict(input_dict, max_x, max_y):
    for y in range(0, max_y):
        row = ''
        for x in range(0, max_x):
            if (x,y) in input_dict.keys():
                row += input_dict[(x,y)]
            else:
                row += '.'
        print(row)

input_dict = {}
max_x = 0
max_y = 0
with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]
    max_y = len(data)
    max_x = len(data[0])
    for y, row in enumerate(data):
        for x, column in enumerate(row):
            if column != '.':
                input_dict[(x,y)] = column

result_dict = step(input_dict, max_x, max_y)
count = 1
while result_dict != input_dict:
    count += 1
    input_dict = result_dict
    result_dict = step(input_dict, max_x, max_y)

print(count)
