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

for minute in range(10):
    tmp_dict = {}

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

result_counter = Counter(loc_dict.values())
print(result_counter['|'] * result_counter['#'])
