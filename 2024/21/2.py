import heapq

num_vals = """789
456
123
 0A"""

robot_vals = """ ^A
<v>"""

def convert_vals(vals):
    result_dict = {}
    for j, row in enumerate(vals.split('\n')):
        for i, column in enumerate(row):
            if column != ' ':
                result_dict[(i, j)] = column

    transfer_dict = {}
    for s_loc in result_dict.keys():
        for e_loc in result_dict.keys():
            if s_loc == e_loc:
                transfer_dict[result_dict[s_loc]*2] = ['']
                continue

            visited = set()

            heap = [(0, s_loc, '')]
            paths = []
            while heap:
                count, curr_loc, path = heapq.heappop(heap)
                visited.add(curr_loc)

                if curr_loc == e_loc:
                    paths.append(path)
                else:
                    neighbours = [
                        ('^', (curr_loc[0], curr_loc[1]-1)),
                        ('>', (curr_loc[0]+1, curr_loc[1])),
                        ('<', (curr_loc[0]-1, curr_loc[1])),
                        ('v', (curr_loc[0], curr_loc[1]+1))
                    ]
                    neighbours = [n for n in neighbours if n[1] in result_dict.keys() and not n[1] in visited]

                    for d, l in neighbours:
                        heapq.heappush(heap, (count+1, l, path + d))

            transfer_dict[result_dict[s_loc]+result_dict[e_loc]] = paths
    return transfer_dict

num_dict = convert_vals(num_vals)
robot_dict = convert_vals(robot_vals)

recurse_dict = {}

def recurse(path, depth, max_depth):
    if (path, depth) in recurse_dict: return recurse_dict[(path, depth)]
    if depth == max_depth: return len(path)
    else:
        answer = 0
        for i, c in enumerate(path):
            presses = num_dict[('A' if i == 0 else path[i-1]) + c] if depth == 0 else robot_dict[('A' if i == 0 else path[i-1]) + c]
            answer += min([recurse(p + 'A', depth + 1, max_depth) for p in presses])
        recurse_dict[(path, depth)] = answer
        return answer
                
with open('input.txt') as f:
    keycodes = [x.strip() for x in f.readlines()]

result = 0
for keycode in keycodes:
    result += recurse(keycode, 0, 26)*int(''.join([x for x in keycode if x.isdigit()]))

print(result)
