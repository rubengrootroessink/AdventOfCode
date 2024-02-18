import copy

def generate_sand_list(bottom_row):
    left, down = 500, 0
    row_length = 1
   
    down += 1
    result_list = [(500,0)]
    while not down == bottom_row:
        left -= 1
        row_length += 2
        for i in range(0, row_length):
            result_list.append((left+i, down))
        down += 1

    return result_list

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

rock_list = []
for item in data:
    points = [[int(y) for y in x.split(',')] for x in item.split(' -> ')]

    points_start = points[0:-1]
    points_end = points[1:]

    for i in range(len(points_start)):
        f = points_start[i]
        s = points_end[i]
        if f[0] == s[0]:
            direction = (s[1]-f[1])//abs(s[1]-f[1])
            for j in range(f[1], s[1]+direction, direction):
                rock_list.append((f[0], j))
        else:
            direction = (s[0]-f[0])//abs(s[0]-f[0])
            for j in range(f[0], s[0]+direction, direction):
                rock_list.append((j, f[1]))

rock_list = list(set(rock_list))
bottom_row = max([y for x,y in rock_list]) + 2
sand_list = generate_sand_list(bottom_row)

minus = 0
for item in sand_list:
    x, y = item
    if (x-1, y-1) in rock_list and (x, y-1) in rock_list and (x+1, y-1) in rock_list:
        minus += 1

print(len(sand_list) - len(rock_list) - minus)
