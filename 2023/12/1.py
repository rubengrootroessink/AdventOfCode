import re
import itertools

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

result = 0
for line in data:
    #print(line)
    chars, groups = line.split(' ')
    groups = [int(x) for x in groups.split(',')]

    total_hashtags = sum(groups)

    q_marks, hash_tags = chars.count('?'), chars.count('#')
    for prod in itertools.product(['.', '#'], repeat=q_marks):
        if hash_tags + prod.count('#') > total_hashtags:
            continue

        tmp_chars = chars
        x = 0
        for i in range(len(tmp_chars)):
            if tmp_chars[i] == '?':
                tmp_chars = tmp_chars[:i] + prod[x] + tmp_chars[i+1:]
                x += 1
        tokens = [len(x) for x in re.split('[\.\?]+', tmp_chars) if x != '']
        if tokens == groups:
            result += 1

print(result)
