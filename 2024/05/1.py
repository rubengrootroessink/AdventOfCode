from collections import defaultdict

order_dict = defaultdict(list)

with open('input.txt') as f:
    order_rules, sections = f.read()[:-1].split('\n\n')
    order_rules = [[int(y) for y in x.split('|')] for x in order_rules.split('\n')]
    for r in order_rules:
        order_dict[r[0]].append(r[1])
    sections = [[int(y) for y in x.split(',')] for x in sections.split('\n')]

res = 0
for pages in sections:
    correct = True
    for i, page in enumerate(pages):
        prev = order_dict[page]
        if any([x in pages[:i] for x in prev]):
            correct = False

    if correct:
        res += pages[(len(pages)-1)//2]

print(res)

