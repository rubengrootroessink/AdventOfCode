import re

def replace(options, replacement_dict, level=1):
    new_options = []
    for option in options:
        for elem in replacement_dict.keys():
            for match in re.finditer(elem, option):
                index = match.span()
                for repl in replacement_dict[elem]:
                    result_string = option[:index[0]] + repl + option[index[1]:]
                    #print(result_string)
                    if result_string == 'e':
                        return level
                    elif 'e' in result_string:
                        pass # Something went wrong, do not include in the new options
                    else:
                        new_options.append(result_string)

    print(level)
    return replace(list(set(new_options)), replacement_dict, level=level+1)

with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')
    replacements = data[0].split('\n')
    
    replacement_dict = {}
    for replacement in replacements:
        item = replacement.split(' => ')
        if item[1] in replacement_dict.keys():
            replacement_dict[item[1]].append(item[0])
        else:
            replacement_dict[item[1]] = [item[0]]

    m = data[1].split('\n')[0]
    elems = list(replacement_dict.keys())

    options = [m]
    print(replace([m], replacement_dict))
