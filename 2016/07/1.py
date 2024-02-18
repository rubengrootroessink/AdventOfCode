import re

with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

pattern = r'(?!(.)\1\1\1)((.)(.)\4\3)'

count = 0
for line in data:
    o_brackets = [[y for y in x if y != ''] for x in re.findall(r'^(\w+)\[|\](\w+)\[|\](\w+)$', line)]
    o_brackets = [item for sublist in o_brackets for item in sublist]
    i_brackets = re.findall(r'\[(\w+)\]', line)
    
    matches = False
    for item in o_brackets:
        if re.search(pattern, item):
            matches = True
    for item in i_brackets:
        if re.search(pattern, item):
            matches = False
    
    if matches:
        count += 1

print(count)
