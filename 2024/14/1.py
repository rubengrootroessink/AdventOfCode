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

result_dict = defaultdict(int)
for i in range(num_robots):
    r = robot_dict[i]
    px, py = r['pos']
    vx, vy = r['vel']
    x, y = (px + vx * 100) % width, (py + vy * 100) % height
    result_dict[(x, y)] += 1

q1 = (range(0, width // 2), range(0, height // 2))
q2 = (range(0, width // 2), range(height // 2 + 1, height))
q3 = (range(width // 2 + 1, width), range(0, height // 2))
q4 = (range(width // 2 + 1, width), range(height // 2 + 1, height))
c1, c2, c3, c4 = 0, 0, 0, 0
for key, value in result_dict.items():
    x, y = key
    if x in q1[0] and y in q1[1]:
        c1 += value
    elif x in q2[0] and y in q2[1]:
        c2 += value
    elif x in q3[0] and y in q3[1]:
        c3 += value
    elif x in q4[0] and y in q4[1]:
        c4 += value

print(c1 * c2 * c3 * c4)
