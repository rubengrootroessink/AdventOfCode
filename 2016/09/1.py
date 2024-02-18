import re

pattern = r'^(\((\d+)x(\d+)\))?'

def parser(non_parsed):
    return_val = 0

    vals = non_parsed.split('(', 1)
    return_val += len(vals[0])
    
    if len(vals) == 2:
        compressed_data = '(' + vals[1]
        matcher = re.match(pattern, compressed_data)
        _, num_chars, num_reps = matcher.groups()
        num_chars, num_reps = int(num_chars), int(num_reps)
        return_val += num_chars*num_reps
        return_val += parser(compressed_data.split(')', 1)[1][num_chars:])
    return return_val

with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

result = 0
for line in data:
    result += parser(line)

print(result)
