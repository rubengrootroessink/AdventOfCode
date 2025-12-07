visited = {}
splitters = []
max_depth = 0

def recurse(start_node):
    if start_node in visited:
        return visited[start_node]
    
    curr_node = start_node
    while not curr_node in splitters and curr_node[1] != max_depth-1:
        curr_node = (curr_node[0], curr_node[1]+1)

    if curr_node in splitters:
        paths = recurse((curr_node[0]-1, curr_node[1])) + recurse((curr_node[0]+1, curr_node[1]))
        visited[start_node] = paths
        return paths 
    elif curr_node[1] == max_depth-1:
        visited[start_node] = 1
        return 1

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

print(recurse(start_node))
