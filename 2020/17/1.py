def check(x, y, z, cube):
    count = 0
    curr_val = '.'

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if not (i == x and j == y and k == z):
                    dict_key = str(i) + ' ' + str(j) + ' ' + str(k)
                    if dict_key in cube.keys():
                        count += 1

    key_val = str(x) + ' ' + str(y) + ' ' + str(z)
    
    if key_val in cube.keys():
        if count == 2 or count == 3:
            return True
        else:
            return False
    else:
        if count == 3:
            return True
        else:
            return False

def cycle(cube):
    new_cube = {}
    for key, value in cube.items():
        for i in range(value['x'] - 1, value['x'] + 2):
            for j in range(value['y'] - 1, value['y'] + 2):
                for k in range(value['z'] - 1, value['z'] + 2):
                    index = str(i) + ' ' + str(j) + ' ' + str(k)
                    if check(i, j, k, cube):
                        new_cube[index] = {'x': i, 'y': j, 'z': k}
    return new_cube

with open('input.txt', 'r') as file:
    cube = {}
    for x, row in enumerate(file.readlines()):
        data = row.split('\n')[0]
        z = 0
        for y, column in enumerate(data):
            if column == '#':
                cube[str(x) + ' ' + str(y) + ' ' + str(z)] = {'x': x, 'y': y, 'z': z}

    cube = cycle(cube)
    cube = cycle(cube)
    cube = cycle(cube)
    cube = cycle(cube)
    cube = cycle(cube)
    cube = cycle(cube)
    
    print(len(cube))
