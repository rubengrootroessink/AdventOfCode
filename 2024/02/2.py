with open('input.txt') as f:
    data = [[int(y) for y in x.split()] for x in f.readlines() if x != '\n']

safe = 0
for line in data:
    for i in range(len(line)):
        new_line = line[0:i] + line[i+1:]

        combi = list(zip(new_line[0:-1], new_line[1:]))

        diff = [x - y for (x, y) in combi]

        dec = all([x > 0 for x in diff])
        inc = all([x < 0 for x in diff])
        val_diff = all([abs(x) in range(1, 4) for x in diff])

        if (dec or inc) and val_diff:
            safe += 1
            break

print(safe)
