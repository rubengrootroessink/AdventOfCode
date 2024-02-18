with open('input.txt', 'r') as f:
    rows = [[int(y) for y in list(x.split('\n')[0])] for x in f.readlines()]

search_dict = {}

visible_trees = 0
size = len(rows)
for i, row in enumerate(rows):
    for j, column in enumerate(row):
        search_dict[(i,j)] = column
        assert len(row) == len(rows)

for key, value in search_dict.items():
    i, j = key[0], key[1]
    if i == 0 or i == size - 1 or j == 0 or j == size - 1:
        visible_trees += 1
    else:
        left = range(0, j)
        left_eval = all([search_dict[(i, k)] < value for k in left])

        right = range(j+1, size)
        right_eval = all([search_dict[(i, k)] < value for k in right])

        up = range(0, i)
        up_eval = all([search_dict[(k, j)] < value for k in up])

        down = range(i+1, size)
        down_eval = all([search_dict[(k, j)] < value for k in down])

        if any([left_eval, right_eval, up_eval, down_eval]):
            visible_trees += 1

print(visible_trees)
