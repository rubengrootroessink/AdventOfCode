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

for i in range(1000):
    new_dict = {}

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

    moon_dict = new_dict

total = 0
for k1, v1 in moon_dict.items():
    px, py, pz = v1['pos']
    pot = abs(px) + abs(py) + abs(pz)

    vx, vy, vz = v1['vel']
    kin = abs(vx) + abs(vy) + abs(vz)

    total += pot * kin

print(total)
