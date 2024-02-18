import re

def recurse(notated_list):
    assert all([x[0] in ['{', '}'] for x in notated_list])
    f_char, f_depth = notated_list[0]
    
    indices = []
    for i, (char, depth) in enumerate(notated_list):
        if depth == f_depth:
            indices.append(i)

    groups = zip(*(iter(indices),)*2)

    count = 0
    for g in groups:
        if g[1] == g[0] + 1:
            count += depth + 1
        else:
            count += recurse(notated_list[g[0]+1:g[1]]) + depth + 1

    assert len(indices) % 2 == 0
    return count

with open('input.txt') as f:
    streams = [x.split('\n')[0] for x in f.readlines()]

for stream in streams:
    clean_stream = re.sub('!.', '', stream)
    clean_stream = re.sub('<.*?>', '', clean_stream)

    notated_list = []

    depth = 0
    for char in clean_stream:
        if char == '{':
            notated_list.append((char, depth))
            depth += 1
        elif char == '}':
            depth -= 1
            notated_list.append((char, depth))
    
    print(recurse(notated_list))
