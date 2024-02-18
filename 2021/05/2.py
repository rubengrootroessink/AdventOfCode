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
    order_x = -1 if x_1 > x_2 else 1
    order_y = -1 if y_1 > y_2 else 1
    l_x = list(range(x_1, x_2 + order_x, order_x))
    l_y = list(range(y_1, y_2 + order_y, order_y))
    l_x = l_x if len(l_x) > 1 else [l_x[0]]*len(l_y)
    l_y = l_y if len(l_y) > 1 else [l_y[0]]*len(l_x)
    l = list(zip(l_x, l_y))
    for item in l:
        id = str(item[0]) + ',' + str(item[1])
        if id in matrix:
            matrix[id] += 1
        else:
            matrix[id] = 1

print(sum(value >= 2 for value in matrix.values()))
