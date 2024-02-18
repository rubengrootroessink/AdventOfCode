import re

with open('input.txt', 'r') as f:
    count = 0
    for line in f.readlines():
        data = line.split('\n')[0]

        match_vowls = re.match(r'(?=([^ ]*[aeiou]){3,})\w*', data)
        match_doubles = re.match(r'[a-z]*([a-z])\1[a-z]*', data)
        match_strings = re.match(r'[a-z]*(ab|cd|pq|xy)[a-z]*', data)

        if match_vowls and match_doubles and not match_strings:
            count += 1
        
    print(count)
