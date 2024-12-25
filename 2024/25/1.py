with open('input.txt') as f:
    items = [x.replace('\n', '') for x in f.read().split('\n\n')]

keys, locks = [],[]
for item in items:
    res = [0,0,0,0,0]
    for i, c in enumerate(item):
        if c == '#':
            res[i%5] += 1

    if item[0:5] == '#'*5 and item[-5:] == '.'*5:
        locks.append(res)
    if item[0:5] == '.'*5 and item[-5:] == '#'*5:
        keys.append(res)

matching = 0
for lock in locks:
    for key in keys:
        merged = [(lock[i]+key[i]) <= 7 for i in range(5)]
        if all(merged):
            matching += 1

print(matching)
