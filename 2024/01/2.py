from collections import defaultdict

with open('input.txt') as f:
    data = [[int(y) for y in x.split()] for x in f.readlines() if x != '\n']

l, r = [], defaultdict(int)
for line in data:
    l.append(line[0])
    r[line[1]] += 1

print(sum([l[i]*r[l[i]] for i in range(len(l))]))
