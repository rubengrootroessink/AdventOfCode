import re

with open('input.txt') as f:
    pattern = r'.*row (\d+), column (\d+)\.'
    row, column = [int(x) for x in re.match(pattern, f.read()).groups()]

nr_rows_and_columns = (column + row - 1)
index = ((((nr_rows_and_columns**2) - nr_rows_and_columns) // 2) + nr_rows_and_columns) - (nr_rows_and_columns - column)

output = 20151125
for i in range(index-1):
    if i % 10000 == 0:
        print(i)
    output = (output*252533)%33554393
print(output)
