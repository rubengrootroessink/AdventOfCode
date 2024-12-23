from collections import defaultdict
from itertools import combinations

with open('input.txt') as f:
    connections = [tuple(x.strip().split('-')) for x in f.readlines()]

graph = defaultdict(list)

for s, e in connections:
    graph[s].append(e)
    graph[e].append(s)

result = None
found = False
for size in range(14, 1, -1):
    for key, value in graph.items():
        if found:
            break

        combs = combinations(value + [key], size)

        for comb in combs:
            if found:
                break

            matches = True
            for i, v1 in enumerate(comb):
                for v2 in comb[i+1:]:
                    if not v2 in graph[v1]:
                        matches = False
 
            if matches:
                result = comb
                found = True
                break

print(','.join(list(sorted(list(result)))))

'''
    result = set()
    for i, v1 in enumerate(value):
        for v2 in result:
            if v2 in graph[v1]:
                result.add(v1)
                result.add(v2)
    print(result)
'''
