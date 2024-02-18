def calculator(val_opp, parity):
    tmp_val = val_opp + parity
    if tmp_val == 4:
        return 1
    elif tmp_val == 0:
        return 3
    else:
        return tmp_val

points = {
    'A': 1,
    'B': 2,
    'C': 3,
}

parity_mapper = {
    'X': -1,
    'Y': 0,
    'Z': 1,
}

score = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

result = 0
with open('input.txt', 'r') as f:
    data = [x.split('\n')[0].split(' ') for x in f.readlines()]
    data = [calculator(points[x[0]], parity_mapper[x[1]]) + score[x[1]] for x in data]
    print(sum(data))
