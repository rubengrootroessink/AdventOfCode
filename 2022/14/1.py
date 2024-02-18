import copy

def new_sand(rock_list, sand_list):
    new_unit = (500, 0)
    result_list = copy.deepcopy(sand_list)

    resting = False
    while not resting:
        if not (new_unit[0], new_unit[1]+1) in rock_list + sand_list:
            new_unit = (new_unit[0], new_unit[1]+1)
        elif not (new_unit[0]-1, new_unit[1]+1) in rock_list + sand_list:
            new_unit = (new_unit[0]-1, new_unit[1]+1)
        elif not (new_unit[0]+1, new_unit[1]+1) in rock_list + sand_list:
            new_unit = (new_unit[0]+1, new_unit[1]+1)
        else:
            resting = True

        if all([new_unit[1] > x[1] for x in rock_list + sand_list]):
            return sand_list

    result_list.append(new_unit)
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
sand_list = []

found = False
while not found:
    new_sand_list = new_sand(rock_list, sand_list)
    if new_sand_list == sand_list:
        found = True
    else:
        sand_list = new_sand_list

print(len(sand_list))
