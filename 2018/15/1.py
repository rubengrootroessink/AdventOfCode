import copy

walls = set()

def move(locs, combatant):
    in_range = {}
    c_type = locs[combatant][0]
    for enemy in [x for (x, y) in locs.items() if y[0] != c_type]:
        i, j = enemy
        ns = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        ns = [(enemy, n) for n in ns if not n in walls and not n in [l for l in locs.keys() if l != combatant]]

        for e, l in ns:
            if not l in in_range.keys():
                in_range[l] = [e]
            else:
                in_range[l].append(e)
    
    if combatant in in_range.keys():
        return combatant

    floodfill_plain = {combatant}
    steps = 0
    while True:
        new_water = set()

        for (i, j) in list(floodfill_plain):
            ns = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            ns = [n for n in ns if not n in walls and not n in locs.keys() and not n in floodfill_plain]
            new_water.update(set(ns))

        steps += 1

        if any(w in in_range.keys() for w in new_water):
            break
        elif new_water == set():
            break
        else:
            floodfill_plain.update(new_water)

    nearest = sorted([w for w in new_water if w in in_range.keys()], key=lambda x: (x[1], x[0]))
    
    if len(nearest) == 0:
        return combatant
    else:
        nearest = nearest[0]

    i, j = combatant
    cns = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    cns = [c for c in cns if not c in walls and not c in locs.keys()]

    if nearest in cns:
        return nearest

    floodfill_plain = {nearest}

    while True:
        new_water = set()
        for (i, j) in list(floodfill_plain):
            ns = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            ns = [n for n in ns if not n in walls and not n in locs.keys() and not n in floodfill_plain]
            new_water.update(set(ns))

        if any([c in new_water for c in cns]):
            cns = [c for c in cns if c in new_water]
            break
        else:
            floodfill_plain.update(new_water)

    return sorted(cns, key=lambda x:(x[1], x[0]))[0]

def attack(locs, new_pos, old_pos):
    i, j = new_pos
    c_type = locs[old_pos][0]
    targets = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    targets = [t for t in targets if t in locs.keys() and not t == old_pos and locs[t][0] != c_type]

    if len(targets) == 0:
        return None
    else:
        min_pos = None
        min_val = None
        for t in targets:
            e_type, hp = locs[t]
            if min_pos == None and min_val == None:
                min_pos = t
                min_val = hp
            elif min_val == hp:
                if t[1] < min_pos[1]:
                    min_pos = t
                elif t[1] == min_pos[1] and t[0] < min_pos[0]:
                    min_pos = t
            elif min_val > hp:
                min_pos = t
                min_val = hp
        return min_pos, e_type, min_val - 3

def turn(locs, combatant):
    new_loc = move(locs, combatant)
    e_info = attack(locs, new_loc, combatant)
    return new_loc, e_info

def round(locs):
    order = sorted(locs.keys(), key=lambda x: (x[1], x[0]))

    new_locs = copy.deepcopy(locs)

    for i, combatant in enumerate(order):
        if not combatant in new_locs.keys():
            continue

        new_loc, e_info = turn(new_locs, combatant)
        new_locs[new_loc] = new_locs[combatant]
        if new_loc != combatant:
            del new_locs[combatant]

        if e_info:
            e_loc, e_type, e_hp = e_info
            if e_hp <= 0:
                del new_locs[e_loc]
                if i < len(order) - 1 and len(set([v[0] for v in new_locs.values()])) == 1:
                    return copy.deepcopy(new_locs), False
            else:
                new_locs[e_loc] = (e_type, e_hp)

    return copy.deepcopy(new_locs), True

with open('input.txt') as f:
    input_data = [x.strip() for x in f.readlines()]

locs = {}
for j, row in enumerate(input_data):
    for i, column in enumerate(row):
        if column == '#':
            walls.add((i, j))
        elif column != '.':
            locs[(i, j)] = (column, 200)

rounds = 0
while True:
    locs, full = round(locs)
    rounds += 1

    if len(set([v[0] for v in locs.values()])) == 1:
        if not full:
            rounds -= 1
        print(rounds * sum([x[1] for x in locs.values()]))
        break
