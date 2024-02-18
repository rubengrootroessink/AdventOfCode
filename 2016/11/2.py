# Inspired by others

import re
import heapq
from itertools import combinations, chain

def is_valid(floor):
    floor = list(floor)

    # Empty state
    if floor == set():
        return True

    # Only microchips or only generators
    elif all([x[1] == floor[0][1] for x in floor]):
        return True

    # All microchips on the floor have an accompanying generator
    else:
        return all([(x[0], 'generator') in floor for x in floor if x[1] == 'microchip'])

def valid_transitions(state):
    steps, elev_loc, floors = state

    c_floor = floors[elev_loc]

    transis = []

    possible_moves = chain(combinations(c_floor, 2), combinations(c_floor, 1))

    for mv in possible_moves:
        for direction in [-1, 1]:
            n_elev_loc = elev_loc + direction    
            if n_elev_loc in range(0, len(floors)):
                n_floors = floors.copy()
                n_floors[elev_loc] = n_floors[elev_loc].difference(mv)
                n_floors[n_elev_loc] = n_floors[n_elev_loc].union(mv)

                if is_valid(n_floors[elev_loc]) and is_valid(n_floors[n_elev_loc]):
                    transis.append((steps + 1, n_elev_loc, n_floors))

    return transis

def end_game(floors):
    return floors[0:3] == [set(),set(),set()]

def count_objects(state):
    ret_val = []
    for f in state:
        ret_val.append((len([x for x in f if x[1] == 'generator']), len([x for x in f if x[1] == 'microchip'])))

    return tuple(ret_val)

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

pattern = r'(\w+)(?:-compatible)? (microchip|generator)'

floors = []
for fl in data:
    floors.append(set(re.findall(pattern, fl)))

floors[0].add(('elerium', 'generator'))
floors[0].add(('elerium', 'microchip'))
floors[0].add(('dilithium', 'generator'))
floors[0].add(('dilithium', 'microchip'))

seen = {(0, 0, count_objects(floors))}
heap = [(0, 0, floors)]
while heap:
    state = heapq.heappop(heap)
    steps, elev_loc, floors = state

    if end_game(floors):
        print(steps)
        break
    
    for n_state in valid_transitions(state):
        c = count_objects(n_state[2])
        if not (n_state[0], n_state[1], c) in seen:
            seen.add((n_state[0], n_state[1], c))
            heapq.heappush(heap, n_state)
