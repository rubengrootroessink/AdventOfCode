def recursive(containers, liters, level=0):
    if liters == 0:
        return [level]
    else:
        result = []
        for i, container in enumerate(containers):
            recursive_result = recursive(containers[i+1:], liters - container, level=level+1)
            if recursive_result:
                for rec_result in recursive_result:
                    result.append(rec_result)
        return result
    return False

with open('input.txt', 'r') as f:
    containers = []
    for line in f.readlines():
        container = int(line.split('\n')[0])
        containers.append(container)
    containers = list(reversed(sorted(containers)))
    liters = 150
    
    nr_combinations = 0
    results = []
    for i, container in enumerate(containers):
        for result in recursive(containers[i+1:], liters - container, level=1):
            results.append(result)
        
    print(results.count(min(results)))
