splitters = []
max_depth = 0
visited = set()

def recurse(start_node):
    curr_node = start_node
    while not curr_node in splitters and curr_node[1] != max_depth-1:
        curr_node = (curr_node[0], curr_node[1]+1)

    if curr_node in visited:
        return True

    if curr_node in splitters:
        recurse((curr_node[0]-1, curr_node[1]))
        recurse((curr_node[0]+1, curr_node[1]))
        visited.add(curr_node)
        return True
    elif curr_node[1] == max_depth-1:
        return True

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

start_node = None
max_depth = len(data)
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column == 'S':
            start_node = (i, j)
        elif column == '^':
            splitters.append((i,j))

recurse(start_node)
print(len(visited))
