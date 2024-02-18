with open('input.txt', 'r') as f:
    rows = [[int(y) for y in list(x.split('\n')[0])] for x in f.readlines()]

def helper(input_list):
    if input_list == []:
        return 0
    else:
        index = 0
        found = False
        for i in range(0, len(input_list)):
            if input_list[i] == False and found == False:
                found = True
                index = i + 1
        if found == False:
            index = len(input_list)
        return index

search_dict = {}

size = len(rows)
for i, row in enumerate(rows):
    for j, column in enumerate(row):
        search_dict[(i,j)] = column
        assert len(row) == len(rows)

scenic_max = 0
for key, value in search_dict.items():
    i, j = key[0], key[1]

    left = range(0, j)
    left_eval = [search_dict[(i, k)] < value for k in left][::-1]

    right = range(j+1, size)
    right_eval = [search_dict[(i, k)] < value for k in right]

    up = range(0, i)
    up_eval = [search_dict[(k, j)] < value for k in up][::-1]

    down = range(i+1, size)
    down_eval = [search_dict[(k, j)] < value for k in down]

    visible_trees = helper(left_eval) * helper(right_eval) * helper(up_eval) * helper(down_eval)
    
    if visible_trees > scenic_max:
        scenic_max = visible_trees

print(scenic_max)
