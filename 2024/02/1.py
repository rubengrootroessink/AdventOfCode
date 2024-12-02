with open('input.txt') as f:
    data = [[int(y) for y in x.split()] for x in f.readlines() if x != '\n']

safe = 0
for line in data:
    combi = list(zip(line[0:-1], line[1:]))
    diff = [x - y for (x, y) in combi]

    dec = all([x > 0 for x in diff])
    inc = all([x < 0 for x in diff])
    val_diff = all([abs(x) in range(1, 4) for x in diff])

    if (dec or inc) and val_diff:
        safe += 1

print(safe)
