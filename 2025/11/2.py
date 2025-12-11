import heapq

conn_dict = {}
dfs_dict = {}

def dfs(curr_node, fft, dac):
    if (curr_node, fft, dac) in dfs_dict:
        return dfs_dict[(curr_node, fft, dac)]

    result = 0
    if curr_node == 'out':
        result = int(fft and dac)
    else:
        result = sum([dfs(end_node, fft or end_node == 'fft', dac or end_node == 'dac') for end_node in conn_dict[curr_node]])

    dfs_dict[(curr_node, fft, dac)] = result
    return result

with open('input.txt') as f:
    conns = [x.strip().split(': ') for x in f.readlines()]

for s, e in conns:
    conn_dict[s] = e.split(' ')

print(dfs('svr', False, False))
