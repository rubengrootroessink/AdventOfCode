import json
import copy
import math

def find_indexes(val, path=''):
    if type(val) == int:
        return ('x', path)
    elif type(val) == list:
        listed_results = [find_indexes(x, path+str(i)) for i, x in enumerate(val)]
        return [item for sublist in listed_results for item in sublist]

def explode_val(val, level=0, path=[]):
    if level == 4 and type(val) == list:
        return path
    elif level == 4 and type(val) == int:
        return False
    elif level < 4:
        if type(val) == int:
            return False
        elif type(val) == list:
            for i, item in enumerate(val):
                exploded_val = explode_val(item, level=level+1, path=path+[i])
                if exploded_val != False:
                    return exploded_val
            return False

def val_from_index(indexes, val):
    if len(indexes) == 1:
        return val[indexes[0]]
    else:
        return val_from_index(indexes[1:], val[indexes[0]])

def change_val(indexes, val, value=0, digit=False):
    new_val = copy.deepcopy(val)
    if len(indexes) == 1:
        if digit:
            new_val[indexes[0]] = value + new_val[indexes[0]]
        else:
            new_val[indexes[0]] = value
    else:
        new_val[indexes[0]] = change_val(indexes[1:], val[indexes[0]], value=value, digit=digit)
    return new_val

def explode(val):
    path = explode_val(val)
    if not path:
        return val
    string_path = ''.join([str(x) for x in path])
    indexes = [x for x in find_indexes(val) if x != 'x']
    explode_index = indexes.index(string_path + '0') # First index of the pair that explodes

    new_val = copy.deepcopy(val)
    left = val_from_index(path + [0], val) if explode_index != 0 else None
    right = val_from_index(path + [1], val) if explode_index + 1 != len(indexes) - 1 else None

    new_val = copy.deepcopy(val)
    if not left is None:
        a = indexes[explode_index - 1]
        a = [int(i) for i in list(a)]
        new_val = change_val(a, new_val, value=left, digit=True)
    if not right is None:
        b = indexes[explode_index + 2]
        b = [int(i) for i in list(b)]
        new_val = change_val(b, new_val, value=right, digit=True)
   
    new_val = change_val(path, new_val)
    return new_val

def splitted_val(val, level=0, path=[]):
    if type(val) == int and val >= 10:
        return (path, val)
    elif type(val) == int:
        return False
    else:
        splitted_vals = [splitted_val(item, path=path+[i]) for i, item in enumerate(val)]
        splitted_vals = [x for x in splitted_vals if x != False]
        return splitted_vals[0] if len(splitted_vals) > 0 else False

def split(val, path=[]):
    path = splitted_val(val)
    if not path:
        return val
    
    new_val = change_val(path[0], val, value=[math.floor(path[1]/2), math.ceil(path[1]/2)], digit=False)
    return new_val

def reduce(val):
    exploded = explode(val)
    if exploded != val:
        return exploded
    splitted = split(val)
    if splitted != val:
        return splitted
    return val

def add(first_val, second_val):
    added = [first_val, second_val]
    reduced = reduce(added)
    while added != reduced:
        added = reduced
        reduced = reduce(reduced)
    return reduced

def magnitude(val):
    result = 0
    if type(val) == int:
        result += val
    else:
        result += sum([3*magnitude(val[0]), 2*magnitude(val[1])])
    return result

with open('input.txt') as f:
    data = [json.loads(x.split('\n')[0]) for x in f.readlines()]

max_mag = 0
for first in data:
    for second in data:
        max_mag = max(max_mag, magnitude(add(first, second)))

print(max_mag)
