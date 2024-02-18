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

parts = parts.split('\n')
for part in parts:
    x, m, a, s = [int(x.split('=')[1]) for x in part[1:-1].split(',')]
    part_dict = {'x': x, 'm': m, 'a': a, 's': s}


    accepted = None

    w = workflow_dict['in']

    found = False
    while not found:
        for comp in w:
            if type(comp) == tuple:
                lt = comp[1] == '<' and part_dict[comp[0]] < comp[2]
                gt = comp[1] == '>' and part_dict[comp[0]] > comp[2]
                if lt or gt:
                    if comp[3] in ['A', 'R']:
                        found = True
                        accepted = comp[3] == 'A'
                    else:
                        w = workflow_dict[comp[3]]
                    break
            else:
                if comp in ['A', 'R']:
                    found = True
                    accepted = comp == 'A'
                else:
                    w = workflow_dict[comp]
                break
    
    assert not accepted is None

    if accepted: 
        result += sum(part_dict.values())

print(result)
