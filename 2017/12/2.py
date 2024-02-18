import heapq

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

data_dict = {}

for line in lines:
    lhs, rhs = line.split('<->')
    lhs = int(lhs)
    rhs = [int(x) for x in rhs.split(', ')]

    if lhs in data_dict.keys():
        data_dict[lhs] = data_dict[lhs].union(set(rhs))
    else:
        data_dict[lhs] = set(rhs)

    for item in rhs:
        if item in data_dict.keys():
            data_dict[item] = data_dict[item].union({lhs})
        else:
            data_dict[item] = {lhs}

final_sets = set()
for key in data_dict.keys():
    final_set = set()
    visited = set()

    heap = [key]
    while heap:
        val = heapq.heappop(heap)
        final_set.add(val)
        visited.add(val)

        for item in data_dict[val]:
            if not item in visited:
                heapq.heappush(heap, item)

    final_sets.add(tuple(sorted(list(final_set))))

print(len(final_sets))
