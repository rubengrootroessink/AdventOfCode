from collections import defaultdict

with open('input.txt') as f:
    data = [[int(y) for y in x.split()] for x in f.readlines() if x != '\n']

l, r = [], []
for line in data:
    l.append(line[0])
    r.append(line[1])

l = sorted(l)
r = sorted(r)

print(sum([abs(l[i]-r[i]) for i in range(len(l))]))
