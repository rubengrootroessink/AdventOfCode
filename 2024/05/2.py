from functools import cmp_to_key
from collections import defaultdict

order_dict = defaultdict(list)

def compare(x, y):
    if y in order_dict[x]:
        return -1
    elif y == x:
        return 0
    else:
        return 1

with open('input.txt') as f:
    order_rules, sections = f.read()[:-1].split('\n\n')
    order_rules = [[int(y) for y in x.split('|')] for x in order_rules.split('\n')]
    for r in order_rules:
        order_dict[r[0]].append(r[1])
    sections = [[int(y) for y in x.split(',')] for x in sections.split('\n')]

res = 0
for pages in sections:
    sorted_pages = list(sorted(pages, key=cmp_to_key(compare)))
    if sorted_pages != pages:
        res += sorted_pages[(len(sorted_pages)-1)//2]

print(res)

