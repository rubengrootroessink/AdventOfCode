import copy

def propose_direction(direction, e, elf, elves):
    vals = []
    if direction == 'N':
        vals = [(elf[0]-1, elf[1]-1), (elf[0], elf[1]-1), (elf[0]+1, elf[1]-1)]
    elif direction == 'S':
        vals = [(elf[0]-1, elf[1]+1), (elf[0], elf[1]+1), (elf[0]+1, elf[1]+1)]
    elif direction == 'W':
        vals = [(elf[0]-1, elf[1]-1), (elf[0]-1, elf[1]), (elf[0]-1, elf[1]+1)]
    elif direction == 'E':
        vals = [(elf[0]+1, elf[1]-1), (elf[0]+1, elf[1]), (elf[0]+1, elf[1]+1)]
    if not any([x in elves for x in vals]):
        return ((vals[1], e))
    else:
        return False

def round(elves, order):
    proposals = []

    for e, elf in enumerate(elves):
        adjacent = [
            (elf[0]-1, elf[1]-1),
            (elf[0]-1, elf[1]),
            (elf[0]-1, elf[1]+1),
            (elf[0], elf[1]-1),
            (elf[0], elf[1]+1),
            (elf[0]+1, elf[1]-1),
            (elf[0]+1, elf[1]),
            (elf[0]+1, elf[1]+1),
        ]

        if not any([x in elves for x in adjacent]):
            proposals.append((elf, 'Assigned'))
        else:
            proposed = False

            for direction in order:
                tmp_result = propose_direction(direction, e, elf, elves)
                if not proposed and tmp_result:
                    proposals.append(tmp_result)
                    proposed = True

            if not proposed:
                proposals.append((elf, e))

    result = []
    proposal_list = [x[0] for x in proposals]
    assert len(proposals) == len(elves)
    for p, proposal in enumerate(proposals):
        if proposal[1] == 'Assigned':
            result.append(proposal[0])
        else:
            if proposal_list.count(proposal[0]) > 1:
                result.append(elves[p])
            else:
                result.append(proposal[0])

    assert len(result) == len(elves)
    
    return result

with open('input.txt', 'r') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

elves = []
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column == '#':
            elves.append((i, j))

order = ['N', 'S', 'W', 'E']
i = 0
found = False
for i in range(10):
    elves_copy = copy.deepcopy(elves)
    elves = round(elves, order)
    order = order[1:] + [order[0]]

x_vals = [x[0] for x in elves]
y_vals = [x[1] for x in elves]
x_min = min(x_vals)
x_max = max(x_vals)
y_min = min(y_vals)
y_max = max(y_vals)

print((x_max + 1 - x_min)*(y_max + 1 - y_min)-len(elves))
