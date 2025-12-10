import heapq
import copy

def resolve(final_state, button_presses):
    start_state = [0 for x in final_state]
    queue = [(0, start_state)]

    visited = {(0, tuple(start_state))}

    while queue:
        presses, curr_state = heapq.heappop(queue)

        if curr_state == final_state:
            return presses

        else:
            for b in button_presses:
                tmp_state = copy.deepcopy(curr_state)
                for conn in b:
                    tmp_state[conn] = 1 if tmp_state[conn] == 0 else 0

                if not (presses+1, tuple(tmp_state)) in visited:
                    queue.append((presses+1, tmp_state))
                    visited.add((presses+1, tuple(tmp_state)))

with open('input.txt') as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

count = 0
for line in lines:
    final_state, button_presses, _ = line[0], line[1:-1], line[-1]
    final_state = [0 if x == '.' else 1 for x in final_state[1:-1]]
    button_presses = [tuple(map(int, b[1:-1].split(','))) for b in button_presses]
    count += resolve(final_state, button_presses)

print(count)
