def incr(old_dict):
    count = 0
    input_dict = old_dict
    luminescent = [k for k,v in input_dict.items() if v == 10]
    vals_to_change = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    for key in luminescent:
        infected = [(key[0]+x, key[1]+y) for x, y in vals_to_change if (key[0]+x, key[1]+y) in input_dict.keys()]
        input_dict[key] = 0
        count += 1
        for item in infected:
            val = input_dict[item]
            input_dict[item] = 0 if val == 0 else 10 if val >= 10 else val + 1
    if 10 in input_dict.values():
        input_dict = incr(input_dict)
    return input_dict

dimensions = (0, 0)
input_dict = {}
with open('input.txt') as file:
    input_matrix = [list(x.split('\n')[0]) for x in file.readlines()]
    dimensions = (len(input_matrix), len(input_matrix[0]))
    for x, row in enumerate(input_matrix):
        for y, column in enumerate(row):
            input_dict[(x,y)] = int(column)

found = False
steps = 0
while not found:
    input_dict = {key: (value + 1 if value != 10 else value) for key, value in input_dict.items()}
    input_dict = incr(input_dict)
    if all([val == 0 for val in input_dict.values()]):
        found = True
    steps += 1

print(steps)
