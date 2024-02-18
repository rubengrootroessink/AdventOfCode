from collections import defaultdict
import math

def grid_to_matcher(grid):
    return '/'.join([''.join(y) for y in grid])

with open('input.txt') as f:
    enhancement_rules = [x.strip().split(' => ') for x in f.readlines()]

enhance_dict = {key: value for (key, value) in enhancement_rules}

start_grid = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#'],
]

curr_grid = start_grid

for i in range(0, 18):
    sub_grids = []

    g_size = len(curr_grid)
    g_div = 2 if len(curr_grid) % 2 == 0 else 3
    for row_num in range(0, g_size, g_div):
        for col_num in range(0, g_size, g_div):
            
            sub_grid = []
            for r in range(row_num, row_num + g_div):
                sub_grid.append(curr_grid[r][col_num:col_num+g_div])

            sub_grids.append(sub_grid)

    result_grid = []
    for g in sub_grids:
        curr_val = ''
        
        rot_1 = list(zip(*reversed(g)))
        rot_2 = list(zip(*reversed(rot_1)))
        rot_3 = list(zip(*reversed(rot_2)))

        flipped = [x[::-1] for x in g]
        f_rot_1 = list(zip(*reversed(flipped)))
        f_rot_2 = list(zip(*reversed(f_rot_1)))
        f_rot_3 = list(zip(*reversed(f_rot_2)))

        for grid in [g, rot_1, rot_2, rot_3, flipped, f_rot_1, f_rot_2, f_rot_3]:
            curr_val = grid_to_matcher(grid)
            if curr_val in enhance_dict.keys():
                result_grid.append(enhance_dict[curr_val])
                break

        assert curr_val != ''

    grid_length = int(math.sqrt(len(result_grid)))
    result_grid = [result_grid[j:j+grid_length] for j in range(0, len(result_grid), grid_length)]

    new_grid = []
    for row in result_grid:
        data_dict = defaultdict(str)
        for column in row:
            data = column.split('/')
            for j, n_row in enumerate(data):
                data_dict[j] = data_dict[j] + n_row

        for _, c in data_dict.items():
            new_grid.append(list(c))

    curr_grid = new_grid

print(sum([sum([1 for x in row if x == '#']) for row in curr_grid]))
