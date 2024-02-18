# Using Karger's algorithm, takes some time to run
import copy
import random

with open('input.txt') as f:
    cmps = [x.split('\n')[0] for x in f.readlines()]

connection_dict = {}
for cmp in cmps:
    f, s = cmp.split(': ')
    s = s.split(' ')
    if f in connection_dict.keys():
        connection_dict[f] = connection_dict[f].union(set(s))
        connection_dict[f].union(set(s))
    else:
        connection_dict[f] = set(s)

    for v in s:
        if v in connection_dict.keys():
            connection_dict[v].add(f)
        else:
            connection_dict[v] = {f}

found = False
while not found:
    
    graph = copy.deepcopy(connection_dict)
    while len(graph) > 2:
        nodes = list(graph.keys())
        u = random.choice(nodes)
        v = random.choice(list(graph[u]))
        new_node = ' '.join(sorted([u, v]))
        new_vals = set([x for x in graph[u].union(graph[v]) if not x == u and not x == v])
        for key, value in graph.items():
            graph[key] = set([new_node if x == u or x == v else x for x in graph[key]])

        graph.pop(u)
        graph.pop(v)
        graph[new_node] = new_vals

    cuts = []

    u, v = graph.keys()
    u = u.split(' ')
    v = v.split(' ')

    assert len(u) + len(v) == len(connection_dict)

    for i in u:
        edges = connection_dict[i]
        for j in v:
            if j in edges and not (j, i) in cuts:
                cuts.append((i, j))

    if len(cuts) == 3:
        found = True
        print(len(u)*len(v))
