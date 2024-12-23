from collections import defaultdict

with open('input.txt') as f:
    connections = [tuple(x.strip().split('-')) for x in f.readlines()]

graph = defaultdict(list)

for s, e in connections:
    graph[s].append(e)
    graph[e].append(s)

sets = []

count = 0
for key, value in graph.items():
    for i, v1 in enumerate(value):
        for v2 in value[i+1:]:
            if v2 in graph[v1]:
                cmp = list(sorted([key, v1, v2]))
                if not cmp in sets:
                    sets.append(cmp)
                    if any([x.startswith('t') for x in cmp]):
                        count += 1

print(count)
