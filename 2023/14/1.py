with open('input.txt') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

rocks = {}
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column in ['#', 'O']:
            rocks[(i, j)] = column

new_rocks = {}
for key, value in rocks.items():

    if value == '#':
        new_rocks[key] = value
    elif value == 'O':
        new_key = (key[0], key[1]-1)
        if new_key[1] < 0:
            new_rocks[key] = value
        elif new_key[1] == 0 and not new_key in new_rocks.keys():
            new_rocks[new_key] = value
        elif new_key in new_rocks.keys():
            new_rocks[key] = value

        while new_key[1] >= 0 and not new_key in new_rocks.keys():
            new_key = (new_key[0], new_key[1]-1)
            if new_key[1] == 0 and not new_key in new_rocks.keys():
                new_rocks[new_key] = value
            elif new_key in new_rocks.keys():
                new_rocks[(new_key[0], new_key[1]+1)] = value

num_rows = len(row)
result = sum([num_rows-k[1] for k, v in new_rocks.items() if v == 'O'])

print(result)
