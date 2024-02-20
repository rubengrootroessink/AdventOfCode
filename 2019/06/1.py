with open('input.txt') as f:
    orbits = [x.strip().split(')') for x in f.readlines()]

orbit_dict = {}

for a, b in orbits:
    orbit_dict[b] = a

total_orbits = 0
for planetoide in orbit_dict.keys():
    
    orbit_count = 0

    curr_val = planetoide
    while curr_val != 'COM':
        curr_val = orbit_dict[curr_val]
        orbit_count += 1

    total_orbits += orbit_count

print(total_orbits)
