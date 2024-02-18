with open('input.txt') as file:
    input_list = [int(x) for x in file.read().split(',')]

def calc_cost(pos_1, pos_2):
    num_pos = abs(pos_1 - pos_2)
    return ((num_pos) * (num_pos + 1)) // 2

fuel_uses = None
max_level = max(input_list)
for level in range(0, max_level):
    val = sum([calc_cost(x, level) for x in input_list])
    fuel_uses = val if fuel_uses == None else min(fuel_uses, val)

print(fuel_uses)
