from collections import defaultdict

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

def in_range(point, max_x, max_y):
    return point[0] in range(0, max_x) and point[1] in range(0, max_y)

max_x, max_y = len(data[0]), len(data)

antenna_dict = defaultdict(list)
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column != '.':
            antenna_dict[column].append((i, j))

result_set = set()
for key, value in antenna_dict.items():
    for a in value:
        for o in value:
            if a != o:
                add_x, add_y = (a[0]-o[0]), (a[1]-o[1])

                val_a, val_o = a, o
                vals = set()

                while True:
                    n_val = (val_a[0]+add_x, val_a[1]+add_y)
                    if in_range(n_val, max_x, max_y):
                        vals.add(n_val)
                        val_a = n_val
                    else:
                        break
                
                while True:
                    n_val = (val_o[0]+add_x, val_o[1]+add_y)
                    if in_range(n_val, max_x, max_y):
                        vals.add(n_val)
                        val_o = n_val
                    else:
                        break

                result_set.update(vals)

print(len(result_set))
