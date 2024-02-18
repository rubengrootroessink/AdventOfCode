with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

expanded_rows = []
for row in data:
    if not '#' in row:
        expanded_rows.append(row)
    expanded_rows.append(row)

transposed_data = [list(sublist) for sublist in list(zip(*expanded_rows))]

expanded_columns = []
for column in transposed_data:
    if not '#' in column:
        expanded_columns.append(column)
    expanded_columns.append(column)

expanded_universe = [list(sublist) for sublist in list(zip(*expanded_columns))]

galaxies = []

for i, row in enumerate(expanded_universe):
    for j, column in enumerate(row):
        if column == '#':
            galaxies.append((i, j))

result = 0
for i, f_galaxy in enumerate(galaxies):
    for s_galaxy in galaxies[i+1:]:
        result += abs(f_galaxy[0]-s_galaxy[0]) + abs(f_galaxy[1]-s_galaxy[1])

print(result)
