with open('input.txt') as f:
    orbits = [x.strip().split(')') for x in f.readlines()]

orbit_dict = {}

for a, b in orbits:
    orbit_dict[b] = a

you = []
san = []

for planetoide in ['YOU', 'SAN']:
    path_to_com = []
    curr_val = planetoide
    while curr_val != 'COM':
        curr_val = orbit_dict[curr_val]
        path_to_com.append(curr_val)

    if planetoide == 'YOU':
        you = path_to_com
    else:
        san = path_to_com

smallest = min(len(you), len(san))
connect_val = None

for i in range(1, smallest+1):
    if you[-i:] != san[-i:]:
        connect_val = you[-i+1]
        break

print(you.index(connect_val) + san.index(connect_val))
