from collections import defaultdict

with open('input.txt') as f:
    robots = [[tuple([int(z) for z in y.split('=')[1].split(',')]) for y in x.strip().split(' ')] for x in f.readlines()]

num_robots = len(robots)

robot_dict = {}
for i in range(num_robots):
    r = robots[i]
    robot_dict[i] = {'pos': r[0], 'vel': r[1]}

width = 101
height = 103

for i in range(0, 10000):
    result_dict = defaultdict(int)
    for j in range(num_robots):
        r = robot_dict[j]
        px, py = r['pos']
        vx, vy = r['vel']
        x, y = (px + vx * i) % width, (py + vy * i) % height
        if result_dict[(x, y)] > 1:
            break

    if len(result_dict) == num_robots:
        print(i)
