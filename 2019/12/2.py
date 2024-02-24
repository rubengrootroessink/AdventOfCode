from math import gcd

with open('input.txt') as f:
    moons = [x.strip() for x in f.readlines()]

moon_dict = {}

for i, moon in enumerate(moons):
    x = int(moon.split('x=')[1].split(',')[0])
    y = int(moon.split('y=')[1].split(',')[0])
    z = int(moon.split('z=')[1].split('>')[0])

    moon_dict[i] = {
        'pos': (x, y, z),
        'vel': (0, 0, 0),
    }

visited = {
    'x': {},
    'y': {},
    'z': {},
}

i = 0

x_cycle = 0
y_cycle = 0
z_cycle = 0

x_found = False
y_found = False
z_found = False

while not x_found or not y_found or not z_found:

    new_dict = {}

    xs = []
    ys = []
    zs = []

    for k1, v1 in moon_dict.items():
        vx, vy, vz = v1['vel']
        ax, ay, az = 0, 0, 0
        for k2, v2 in moon_dict.items():
            if k1 != k2:
                k1x, k2x = v1['pos'][0], v2['pos'][0]
                ax += 1 if k2x > k1x else 0 if k2x == k1x else -1
                
                k1y, k2y = v1['pos'][1], v2['pos'][1]
                ay += 1 if k2y > k1y else 0 if k2y == k1y else -1
                
                k1z, k2z = v1['pos'][2], v2['pos'][2]
                az += 1 if k2z > k1z else 0 if k2z == k1z else -1

        new_dict[k1] = {}
        new_dict[k1]['vel'] = (vx+ax, vy+ay, vz+az)
        px, py, pz = v1['pos']
        new_dict[k1]['pos'] = (px+vx+ax, py+vy+ay, pz+vz+az)

        xs.append((px+vx+ax, vx+ax))
        ys.append((py+vy+ay, vy+ay))
        zs.append((pz+vz+az, vz+az))

    moon_dict = new_dict

    if not x_found and tuple(xs) in visited['x'].keys():
        x_found = True
        x_cycle = i - visited['x'][tuple(xs)]
    
    if not y_found and tuple(ys) in visited['y'].keys():
        y_found = True
        y_cycle = i - visited['y'][tuple(ys)]
    
    if not z_found and tuple(zs) in visited['z'].keys():
        z_found = True
        z_cycle = i - visited['z'][tuple(zs)]

    visited['x'][tuple(xs)] = i
    visited['y'][tuple(ys)] = i
    visited['z'][tuple(zs)] = i
    
    i += 1

cycles = [x_cycle, y_cycle, z_cycle]
lcm = x_cycle
for i in cycles[1:]:
    lcm = lcm*i//gcd(lcm, i)

print(lcm)
