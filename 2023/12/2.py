# Inspired by others

dp_dict = {}

def funct(chars, groups, ci, gi, curr_len):
    
    global dp_dict

    key = (ci, gi, curr_len)
    
    if key in dp_dict.keys():
        return dp_dict[key]
    
    if ci == len(chars):
        if (gi == len(groups) and curr_len == 0) or (gi == len(groups)-1 and groups[gi] == curr_len):
            return 1
        else:
            return 0
    
    result = 0
    for c in ['.', '#']:
        if chars[ci] == c or chars[ci] == '?':
            
            # Current char is a dot
            # We are currently not in a group of '#'s
            if c == '.' and curr_len == 0:
                result += funct(chars, groups, ci+1, gi, 0)
            
            # Current char is a dot
            # We are in a group of '#'s
            # The current group is lower than the number of groups
            # The group at our current group index equals the length of the current group
            elif c == '.' and curr_len > 0 and gi < len(groups) and groups[gi] == curr_len:
                result += funct(chars, groups, ci+1, gi+1, 0)

            # Current char is a hashtag
            elif c == '#':
                result += funct(chars, groups, ci+1, gi, curr_len+1)

    dp_dict[key] = result
    return result

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

result = 0
for line in data:
    chars, groups = line.split()

    chars = '?'.join([chars]*5)
    groups = ','.join([groups]*5)

    groups = [int(x) for x in groups.split(',')]

    dp_dict = {}
    result += funct(chars, groups, 0, 0, 0)

print(result)
