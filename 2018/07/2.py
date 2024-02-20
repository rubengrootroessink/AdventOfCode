import re
import heapq
import string

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

pattern = r'^Step (\w) must be finished before step (\w) can begin.$'

unique_vals = set()

dep_dict = {}
for instr in instrs:
    a, b = re.match(pattern, instr).groups()

    if b in dep_dict.keys():
        dep_dict[b].add(a)
    else:
        dep_dict[b] = {a}

    unique_vals.add(a)
    unique_vals.add(b)

dep_dict = {k: v for (k, v) in sorted(dep_dict.items())}

start_val = ''.join(sorted(list(unique_vals.difference(set(dep_dict.keys())))))

order = ''

num_workers = 6

workers = {}
for i in range(0, num_workers):
    workers[i] = {'task': '.', 'depth': 0}

for i in range(0, len(start_val)):
    workers[i]['task'] = start_val[i]
    workers[i]['depth'] = string.ascii_uppercase.index(start_val[i])+60

i = 0
running_tasks = [start_val]
while not len(order) == len(unique_vals):

    for j, v in workers.items():
        if v['depth'] == 0 and v['task'] != '.':
            order += v['task']
            running_tasks = [x for x in running_tasks if x != v['task']]
            workers[j]['task'] = '.'

    available_tasks = sorted([k for k, v in dep_dict.items() if v-set(order) == set()])
    available_tasks = [x for x in available_tasks if not x in order and not x in running_tasks]

    for j, v in workers.items():
        if v['depth'] == 0:
            try:
                new_task = heapq.heappop(available_tasks)
                workers[j]['task'] = new_task
                workers[j]['depth'] = string.ascii_uppercase.index(new_task)+60
                running_tasks.append(new_task)
            except:
                workers[j]['task'] = '.'
        else:
            workers[j]['depth'] -= 1
    
    i += 1

print(i)
