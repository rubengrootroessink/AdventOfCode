import heapq

with open('input.txt') as f:
    conns = [x.strip().split(': ') for x in f.readlines()]

conn_dict = {}
for s, e in conns:
    conn_dict[s] = e.split(' ')

count = 0
queue = ['you']
while queue:
    curr_node = heapq.heappop(queue)
    if curr_node == 'out':
        count += 1
    else:
        for val in conn_dict[curr_node]:
            heapq.heappush(queue, val)

print(count)
