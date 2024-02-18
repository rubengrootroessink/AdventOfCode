with open('input.txt') as f:
    path = f.read().strip().split(',')

path_dict = {
    'n': 0,
    's': 0,
    'ne': 0,
    'sw': 0,
    'nw': 0,
    'se': 0,
}

for val in path:

    if val == 'n':
        if path_dict['s'] != 0:
            path_dict['s'] -= 1
        elif path_dict['se'] != 0:
            path_dict['se'] -= 1
            path_dict['ne'] += 1
        elif path_dict['sw'] != 0:
            path_dict['sw'] -= 1
            path_dict['nw'] += 1
        else:
            path_dict['n'] += 1
            
    elif val == 's':
        if path_dict['n'] != 0:
            path_dict['n'] -= 1
        elif path_dict['ne'] != 0:
            path_dict['ne'] -= 1
            path_dict['se'] += 1
        elif path_dict['nw'] != 0:
            path_dict['nw'] -= 1
            path_dict['sw'] += 1
        else:
            path_dict['s'] += 1
    
    elif val == 'ne':
        if path_dict['sw'] != 0:
            path_dict['sw'] -= 1
        elif path_dict['s'] != 0:
            path_dict['s'] -= 1
            path_dict['se'] += 1
        else:
            path_dict['ne'] += 1

    elif val == 'se':
        if path_dict['nw'] != 0:
            path_dict['nw'] -= 1
        elif path_dict['n'] != 0:
            path_dict['n'] -= 1
            path_dict['ne'] += 1
        else:
            path_dict['se'] += 1

    elif val == 'nw':
        if path_dict['se'] != 0:
            path_dict['se'] -= 1
        elif path_dict['s'] != 0:
            path_dict['s'] -= 1
            path_dict['sw'] += 1
        else:
            path_dict['nw'] += 1

    elif val == 'sw':
        if path_dict['ne'] != 0:
            path_dict['ne'] -= 1
        elif path_dict['n'] != 0:
            path_dict['n'] -= 1
            path_dict['nw'] += 1
        else:
            path_dict['sw'] += 1

print(sum(path_dict.values()))
