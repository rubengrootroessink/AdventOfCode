input_matrix = []
with open('input.txt') as file:
    input_matrix = [[int(y) for y in list(x.split('\n')[0])] for x in file.readlines()]

result = 0
for i, row in enumerate(input_matrix):
    for j, column in enumerate(row):
        row_vals = [input_matrix[i][x] for x in list(range(max(0, j-1), min(len(row), j+2))) if x != j]
        col_vals = [input_matrix[x][j] for x in list(range(max(0, i-1), min(len(input_matrix), i+2))) if x != i]
        if all(elem > column for elem in row_vals + col_vals):
            result += column + 1

print(result)

