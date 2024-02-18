with open('input.txt') as file:
    input_list = [int(x) for x in file.read().split(',')]

fuel_uses = None
max_level = max(input_list)
for level in range(-max_level, max_level * 2):
    print(level, fuel_uses)
    #print([abs(x-level) for x in input_list])
    val = sum([abs(x-level) for x in input_list])
    fuel_uses = val if fuel_uses == None else min(fuel_uses, val)

print(fuel_uses)
