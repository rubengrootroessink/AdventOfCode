from functools import reduce

def find_surrounding(i, j, matrix, checked):
    top = bottom = left = right = None
    if j > 0 and not (i, j-1) in checked:
        left = (i, j-1) if matrix[i][j-1] != 9 else None
    if j < len(matrix[0])-1 and not (i, j+1) in checked:
        right = (i, j+1) if matrix[i][j+1] != 9 else None
    if i > 0 and not (i-1, j) in checked:
        top = (i-1, j) if matrix[i-1][j] != 9 else None
    if i < len(matrix)-1 and not (i+1, j) in checked:
        bottom = (i+1, j) if matrix[i+1][j] != 9 else None
    return [x for x in [top, bottom, left, right] if x != None]

input_matrix = []
with open('input.txt') as file:
    input_matrix = [[int(y) for y in list(x.split('\n')[0])] for x in file.readlines()]

low_points = []
for i, row in enumerate(input_matrix):
    for j, column in enumerate(row):
        row_vals = [input_matrix[i][x] for x in list(range(max(0, j-1), min(len(row), j+2))) if x != j]
        col_vals = [input_matrix[x][j] for x in list(range(max(0, i-1), min(len(input_matrix), i+2))) if x != i]
        if all(elem > column for elem in row_vals + col_vals):
            low_points.append((i, j))

result = []
for point in low_points:
    basin = checked_points = [point]
    points_to_check = find_surrounding(point[0], point[1], input_matrix, checked_points)
    while points_to_check != []:
        checked_points = checked_points + points_to_check
        new_vals = []
        for p in points_to_check:
            new_vals += find_surrounding(p[0], p[1], input_matrix, checked_points)
        points_to_check = new_vals
    result.append(len(set(checked_points)))
result = list(sorted(result))[-3:]
print(reduce((lambda x, y: x * y), result))
