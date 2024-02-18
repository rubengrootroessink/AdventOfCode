def step(x_pos, y_pos, x_velo, y_velo):
    new_x_pos = x_pos + x_velo
    new_y_pos = y_pos + y_velo
    new_x_velo = x_velo - 1 if x_velo > 0 else 0 if x_velo == 0 else x_velo + 1
    new_y_velo = y_velo - 1
    return new_x_pos, new_y_pos, new_x_velo, new_y_velo

def find_max(velo_x, velo_y, target):
    x_pos, y_pos = 0, 0
    x_velo, y_velo = velo_x, velo_y
   
    y_max = 0

    found = False

    while y_pos >= min(target[1][0], target[1][1]) and not found:
        x_pos, y_pos, x_velo, y_velo = step(x_pos, y_pos, x_velo, y_velo)
        y_max = max(y_max, y_pos)
        if target[0][0] <= x_pos <= target[0][1] and min(target[1][0], target[1][1]) <= y_pos <= max(target[1][0], target[1][1]):
            found = True

    if found:
        return True, y_max
    else:
        return False, 0

target = []
with open('input.txt') as f:
    data = f.read().split('\n')[0]
    target = [[int(val) for val in item.split('..')] for item in data.split('area: x=')[1].split(', y=')]

pairs = []
y_max = 0
for x in range(0, target[0][1] + 1):
    for y in range(min(target[1][0], target[1][1]), max(abs(target[1][0]), abs(target[1][1]))):
        result, new_y_max = find_max(x, y, target)
        if result:
            if x == 5 and y == 7:
                print(x, y)
            pairs.append((x, y))

print(len(pairs))
