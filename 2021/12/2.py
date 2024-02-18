import copy

def checker(val, curr_path):
    if val.isupper() or val == 'end':
        return True

    lowers = [x for x in curr_path if x != 'start' and x != 'end' and x.islower()]
    if len(lowers) == len(set(lowers)):
        return True
    else:
        return not (val in curr_path and val.islower())

def rec_path(curr_path, input_dict):
    if curr_path[-1] == 'end':
        return [curr_path]

    paths = []
    for poss_val in [x for x in input_dict[curr_path[-1]] if checker(x, curr_path)]:
        paths += rec_path(curr_path + [poss_val], copy.deepcopy(input_dict))
    return paths

input_dict = {}
with open('input.txt') as file:
    vals = [x.split('\n')[0].split('-') for x in file.readlines()]
    for val in vals:
        if not(val[1] == 'start' or val[0] == 'end'):
            if not val[0] in input_dict.keys():
                input_dict[val[0]] = [val[1]]
            else:
                input_dict[val[0]].append(val[1])

        if not(val[0] == 'start' or val[1] == 'end'):
            if not val[1] in input_dict.keys():
                input_dict[val[1]] = [val[0]]
            else:
                input_dict[val[1]].append(val[0])

paths = []
start_vals = input_dict['start']
input_dict.pop('start')
for item in start_vals:
    paths += rec_path(['start',item], copy.deepcopy(input_dict))

print(len(paths))
