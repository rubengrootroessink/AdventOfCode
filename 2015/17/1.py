def recursive(containers, liters):
    if liters < 0:
        return 0
    elif liters == 0:
        return 1
    else:
        result = 0
        for i, container in enumerate(containers):
            result += recursive(containers[i+1:], liters - container)
        return result

with open('input.txt', 'r') as f:
    containers = []
    for line in f.readlines():
        container = int(line.split('\n')[0])
        containers.append(container)
    containers = list(reversed(sorted(containers)))
    liters = 150
    
    nr_combinations = 0
    for i, container in enumerate(containers):
        nr_combinations += recursive(containers[i+1:], liters - container)
    print(nr_combinations)
