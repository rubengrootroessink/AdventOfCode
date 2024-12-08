from collections import defaultdict

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

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
                val_a = (a[0]+add_x, a[1]+add_y)
                if val_a[0] in range(0, max_x) and val_a[1] in range(0, max_y):
                    result_set.add(val_a)
                val_b = (o[0]-add_x, o[1]-add_y)
                if val_b[0] in range(0, max_x) and val_b[1] in range(0, max_y):
                    result_set.add(val_b)

print(len(result_set))
