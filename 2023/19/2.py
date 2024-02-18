# Inspired by others

import copy
import math
import heapq

with open('input.txt') as f:
    workflows, parts = f.read()[:-1].split('\n\n')

workflow_dict = {}
workflows = workflows.split('\n')
for w in workflows:
    name, rest = w.split('{')
    comps = rest[:-1].split(',')
    parsed_comps = []
    for comp in comps:
        if ':' in comp:
            var = comp[0]
            order = comp[1]
            nr, redirect = comp[2:].split(':')
            nr = int(nr)
            parsed_comps.append((var, order, nr, redirect))
        else:
            parsed_comps.append((comp))

    workflow_dict[name] = parsed_comps

result = 0
heap = [('in', [(1,4000), (1,4000), (1,4000), (1,4000)])]
while heap:
    loc, vals = heapq.heappop(heap)

    assert [val[1] >= val[0] for val in vals]

    if loc == 'A':
        curr_result = math.prod([val[1]+1-val[0] for val in vals])
        result += curr_result
    elif loc == 'R':
        pass
    else:
        wf = workflow_dict[loc]
        for comp in wf:
            if type(comp) == tuple:
                num = ['x', 'm', 'a', 's'].index(comp[0])
                new_vals = copy.deepcopy(vals)
                if comp[2] in range(new_vals[num][0], new_vals[num][1]+1):
                    if comp[1] == '<':
                        range_a = (new_vals[num][0], comp[2]-1)
                        range_b = (comp[2], new_vals[num][1])
                        new_vals[num] = range_a
                        heapq.heappush(heap, (comp[3], new_vals))
                        vals[num] = range_b
                    elif comp[1] == '>':
                        range_a = (new_vals[num][0], comp[2])
                        range_b = (comp[2]+1, new_vals[num][1])
                        new_vals[num] = range_b
                        heapq.heappush(heap, (comp[3], new_vals)) 
                        vals[num] = range_a
            elif type(comp) == str:
                heapq.heappush(heap, (comp, vals))

print(result)
