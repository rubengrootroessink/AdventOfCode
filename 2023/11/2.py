with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

galaxies = []

for i, row in enumerate(data):
    for j, column in enumerate(row):
        if column == '#':
            galaxies.append((i, j))

empty_row_indices = []
for i, row in enumerate(data):
    if not '#' in row:
        empty_row_indices.append(i)

empty_column_indices = []
for j, column in enumerate([list(sublist) for sublist in list(zip(*data))]):
    if not '#' in column:
        empty_column_indices.append(j)

expand_val = 1000000

result = 0
for i, f_galaxy in enumerate(galaxies):
    for s_galaxy in galaxies[i+1:]:
        expanded_rows = sum([1 for y in empty_row_indices if y in range(min(f_galaxy[0], s_galaxy[0]), max(f_galaxy[0], s_galaxy[0]))])*(expand_val-1)
        expanded_columns = sum([1 for x in empty_column_indices if x in range(min(f_galaxy[1], s_galaxy[1]), max(f_galaxy[1], s_galaxy[1]))])*(expand_val-1)

        result += abs(f_galaxy[0]-s_galaxy[0]) + expanded_rows + abs(f_galaxy[1]-s_galaxy[1]) + expanded_columns

print(result)
