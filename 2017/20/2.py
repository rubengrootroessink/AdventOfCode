from collections import Counter
import re

def change(particles):
    res_list = []

    for p in particles:
        px, py, pz = p[0]
        vx, vy, vz = p[1]
        ax, ay, az = p[2]

        vx += ax
        vy += ay
        vz += az

        px += vx
        py += vy
        pz += vz

        man_dist = sum([abs(px), abs(py), abs(pz)])

        res_list.append([(px, py, pz), (vx, vy, vz), p[2], man_dist])
    
    return res_list

def clean_collisions(particles):
    pos = Counter([p[0] for p in particles])

    res_list = []
    for p in particles:
        if pos[p[0]] == 1:
            res_list.append(p)

    return res_list

pattern = r'^p=<(.+)>, v=<(.+)>, a=<(.+)>$'
with open('input.txt') as f:
    particles = [[[int(z) for z in y.split(',')] for y in re.match(pattern, x.strip()).groups()] for x in f.readlines()]

particles = [[tuple(y) for y in x] + [sum([abs(z) for z in x[0]])] for x in particles]

count = 0
while count < 1000:
    particles = change(particles)
    num_particles = len(particles)

    particles = clean_collisions(particles)
    if len(particles) == num_particles:
        count += 1

print(len(particles))
