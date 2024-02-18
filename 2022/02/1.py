points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

mapper = {
    0: 3, # Draw
    1: 6, # Win for us
    -2: 6, # Loss for them
    -1: 0, # Win for them
    2: 0, # Loss for us
}

result = 0
with open('input.txt', 'r') as f:
    data = [[points[y] for y in x.split('\n')[0].split(' ')] for x in f.readlines()]
    [result := result + y[1] + mapper[y[1]-y[0]] for y in data]
    print(result)
