import copy

def propose_direction(direction, elf, elves):
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
        return vals[1]
    else:
        return False

def round(elves, order):
    proposals = {}

    for elf in elves:
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
            proposals[elf] = elf
        else:
            proposed = False

            for direction in order:
                tmp_result = propose_direction(direction, elf, elves)
                if not proposed and tmp_result:
                    proposals[elf] = tmp_result
                    proposed = True

            if not proposed:
                proposals[elf] = elf

    result = []
    proposal_list = list(proposals.values())
    assert len(proposals) == len(elves)
    for elf, proposal in proposals.items():
        if elf == proposal:
            result.append(elf)
        else:
            if proposal_list.count(proposal) > 1:
                result.append(elf)
            else:
                result.append(proposal)

    return result

with open('input.txt', 'r') as f:
    rows = [x.split('\n')[0] for x in f.readlines()]

elves = set()
for j, row in enumerate(rows):
    for i, column in enumerate(row):
        if column == '#':
            elves.add((i, j))

order = ['N', 'S', 'W', 'E']
i = 0
found = False
while not found:
    elves_copy = copy.deepcopy(elves)
    elves = round(elves, order)
    order = order[1:] + [order[0]]
    if elves_copy == elves:
        found = True
    else:
        i += 1

# Very slow
print(i+1)
