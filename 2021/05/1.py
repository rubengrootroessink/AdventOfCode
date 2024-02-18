with open('input.txt') as file:
    input_list = [x.split('\n')[0].split(' -> ') for x in file.readlines()]
    cleaned_list = []
    for item in input_list:
        x_1, y_1 = [int(x) for x in item[0].split(',')]
        x_2, y_2 = [int(x) for x in item[1].split(',')]
        cleaned_list.append([x_1, y_1, x_2, y_2])

matrix = {}
for item in cleaned_list:
    x_1, y_1, x_2, y_2 = item
    if x_1 == x_2 or y_1 == y_2:
        x_1, x_2 = sorted([x_1, x_2])
        y_1, y_2 = sorted([y_1, y_2])
        l_x = list(range(x_1, x_2 + 1))
        l_y = list(range(y_1, y_2 + 1))
        for x in l_x:
            for y in l_y:
                id = str(x) + ',' + str(y)
                if id in matrix:
                    matrix[id] += 1
                else:
                    matrix[id] = 1

print(sum(value >= 2 for value in matrix.values()))
