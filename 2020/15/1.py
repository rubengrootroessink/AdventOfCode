with open('input.txt', 'r') as file:
    data = [int(x) for x in file.read().split(',')]
    while len(data) < 2020:
        if data.count(data[-1]) == 1:
            data.append(0)
        else:
            indices = [i for i, x in enumerate(data) if x == data[-1]][-2:]
            data.append(indices[1] - indices[0])
    print(data)
