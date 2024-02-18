from itertools import permutations

with open('input.txt') as f:
    people = {}
    for data in f.readlines():
        line = data.split('.\n')[0].split(' ')
        p1 = line[0]
        p2 = line[-1]
        op = line[2]
        value = int(line[3])
        if p1 in people.keys():
            people[p1][p2] = {'op': op, 'val': value}
        else:
            people[p1] = {p2: {'op': op, 'val': value}}

    for person in people.keys():
        people[person]['You'] = {'op': 'gain', 'val': 0}

    persons = list(people.keys())
    for person in persons:
        if not 'You' in people.keys():
            people['You'] = {}
        people['You'][person] = {'op': 'gain', 'val': 0}

    perm = [list(x) for x in permutations(people.keys())]
    
    final_val = 0
    final_setting = []
    for elem in list(perm):
        orig_list = elem
        new_list = elem[1:] + [elem[0]]
        
        concattenated_list = [(orig_list[i], new_list[i]) for i in range(0, len(orig_list))]
        
        result = 0
        for item in concattenated_list:
            value = people[item[0]][item[1]]
            if value['op'] == 'gain':
                result += value['val']
            elif value['op'] == 'lose':
                result -= value['val']

            value = people[item[1]][item[0]]
            if value['op'] == 'gain':
                result += value['val']
            elif value['op'] == 'lose':
                result -= value['val']
        if result > final_val:
            final_val = result
            final_setting = elem
            
    print(final_val)
