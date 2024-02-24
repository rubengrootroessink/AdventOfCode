from collections import Counter

def get_neighbours(node):
    x, y = node

    return [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x-1, y),
        (x+1, y),
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1),
    ]

with open('input.txt') as f:
    area = [x.strip() for x in f.readlines()]

loc_dict = {}

for j, row in enumerate(area):
    for i, column in enumerate(row):
        loc_dict[(i, j)] = column

visited = {}

i = 0
while i < 1000000000:
    tmp_dict = {}

    hash_val = ''.join(loc_dict.values())

    if hash_val in visited.keys():
        cycle_length = i - visited[hash_val]
        i = i + ((1000000000 - i) // cycle_length)*cycle_length

    visited[hash_val] = i

    for key, value in loc_dict.items():

        neighbours = [loc_dict[x] for x in get_neighbours(key) if x in loc_dict.keys()]

        counter = Counter(neighbours)

        if value == '.':
            if counter['|'] >= 3:
                tmp_dict[key] = '|'
            else:
                tmp_dict[key] = '.'

        elif value == '|':
            if counter['#'] >= 3:
                tmp_dict[key] = '#'
            else:
                tmp_dict[key] = '|'
        
        elif value == '#':
            if counter['#'] > 0 and counter['|'] > 0:
                tmp_dict[key] = '#'
            else:
                tmp_dict[key] = '.'

    loc_dict = tmp_dict

    i += 1

result_counter = Counter(loc_dict.values())
print(result_counter['|'] * result_counter['#'])
