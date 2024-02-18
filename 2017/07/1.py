import re

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

    weight_dict[name] = weight

for key in support_dict.keys():
    if all([not key in v for v in support_dict.values()]):
        print(key) 
