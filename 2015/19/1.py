with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')
    replacements = data[0].split('\n')
    
    replacement_dict = {}
    for replacement in replacements:
        item = replacement.split(' => ')
        if item[0] in replacement_dict.keys():
            replacement_dict[item[0]].append(item[1])
        else:
            replacement_dict[item[0]] = [item[1]]
    
    m = data[1].split('\n')[0]
    elems = list(replacement_dict.keys())

    count = 0
    found = False
    molecule = []
    while not found:
        if m[count] in elems:
            molecule.append(elems.index(m[count]))
            count += 1
        elif m[count:count+2] in elems:
            molecule.append(elems.index(m[count:count+2]))
            count += 2
        else:
            molecule.append(m[count])
            count += 1
        if count >= len(m):
            found = True
    
    resulting_molecules = []
    for i, elem in enumerate(replacement_dict.keys()):
        indices = [pos for pos, char in enumerate(molecule) if char == elems.index(elem)]
        for index in indices:
            for replacement in replacement_dict[elem]:
                temp_m = molecule[:index] + [replacement] + molecule[index+1:]
                temp_m = [x if type(x) == str else elems[x] for x in temp_m]
                temp_str = "".join(temp_m)
                resulting_molecules.append(temp_str)

    print(len(set(resulting_molecules)))
