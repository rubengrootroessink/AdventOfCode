# Inspired by others, algorithm takes some run time in order to finish

from z3 import Int, Solver

with open('input.txt') as f:
    hailstones = [x.split('\n')[0] for x in f.readlines()]

parsed_hailstones = []
for stone in hailstones:
    c, v = stone.split(' @ ')
    cx, cy, cz = [int(x) for x in c.split(', ')]
    vx, vy, vz = [int(x) for x in v.split(', ')]

    parsed_hailstones.append(((cx, cy, cz), (vx, vy, vz)))

hailstones = parsed_hailstones

# Result variables containing:
# - Start position of the rock: x, y, z
# - Velocities in the three different directions: vx, vy, vz
x, y, z, vx, vy, vz = [Int(i) for i in ['x', 'y', 'z', 'vx', 'vy', 'vz']]

# z3 solver
s = Solver()

# Time integers
t = [Int('T' + str(i)) for i in range(6)] # Took only the first 6 hail stones as they are enough to finish our equation

# For each of the hailstones
for i, stone in enumerate(hailstones[:6]): # Took only the first 6 hail stones as they are enough to finish our equation
    (sx, sy, sz), (svx, svy, svz) = stone
    
    # Add an equation for the x, y and z position respectively
    s.add(x + t[i]*vx == t[i]*svx + sx)
    s.add(y + t[i]*vy == t[i]*svy + sy)
    s.add(z + t[i]*vz == t[i]*svz + sz)


res = s.check()
M = s.model()
print(M.eval(x+y+z))
