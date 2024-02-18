def build_paths(curr_path, distances, nodes):
    result = []
    last = curr_path[-1]
    options = [x for x in distances[last] if not x in curr_path]
    
    if len(curr_path) == len(nodes) - 1:
        for option in options:
            result.append(curr_path + [option])
    else:
        for option in options:
            paths = build_paths(curr_path + [option], distances, nodes)
            for path in paths:
                result.append(path)
            
    return result
    
def eval_path(path, distances):
    if len(path) == 2:
        return distances[path[0]][path[1]]
    else:
        return distances[path[0]][path[1]] + eval_path(path[1:], distances)


distances = {}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    nodes = []
    
    tuples = []
    for line in lines:
        data = line.split('\n')[0].split(' ')
        start = data[0]
        end = data[2]
        weight = int(data[4])
        nodes.append(start)
        nodes.append(end)
        if start in distances.keys():
            distances[start][end] = weight
        else:
            distances[start] = {end : weight}
        if end in distances.keys():
            distances[end][start] = weight
        else:
            distances[end] = {start: weight}
            
    nodes = list(set(nodes))

    results = []
    for node in nodes:
        paths = build_paths([node], distances, nodes)
        for path in paths:
            results.append(eval_path(path, distances))
    print(max(results))
