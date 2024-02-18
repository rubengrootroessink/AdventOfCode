import re
from collections import Counter

def calc_weight(input_node, weight_dict, support_dict):
    result = weight_dict[input_node]
    if input_node in support_dict.keys():
        result += sum([calc_weight(x, weight_dict, support_dict) for x in support_dict[input_node]])
    return result

with open('input.txt') as f:
    programs = [x.split('\n')[0] for x in f.readlines()]

weight_dict = {}
support_dict = {}

for prog in programs:
    information = prog
    supports = None

    if ' -> ' in prog:
        information, supports = prog.split(' -> ')
        supports = supports.split(', ')
    
    pattern = r'^(\w+) \((\d+)\)?$'
    name, weight = re.match(pattern, information).groups()

    if not supports is None:
        support_dict[name] = supports

    weight_dict[name] = int(weight)

bottom_prog = None
for key in support_dict.keys():
    if all([not key in v for v in support_dict.values()]):
        bottom_prog = key

curr_prog = bottom_prog
found = False
while not found:
    wrong_tower = None
    weights = {x: calc_weight(x, weight_dict, support_dict) for x in support_dict[curr_prog]}
    sorted_weights = sorted(weights.items(), key = lambda x: x[1])
    correct_weight = sorted_weights[1][1]
    if sorted_weights[0][1] == correct_weight:
        wrong_tower = sorted_weights[-1][0]
    else:
        wrong_tower = sorted_weights[0][0]

    if len(set([calc_weight(x, weight_dict, support_dict) for x in support_dict[wrong_tower]])) == 1:
        found = True
        print(correct_weight-weights[wrong_tower]+weight_dict[wrong_tower])
    else:
        curr_prog = wrong_tower
