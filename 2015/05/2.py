import re

with open('input.txt', 'r') as f:
    count = 0
    for line in f.readlines():
        data = line.split('\n')[0]

        match_pairs = re.match(r'[a-z]*([a-z]{2})[a-z]*\1[a-z]*', data)
        match_consec = re.match(r'[a-z]*([a-z])[a-z]\1[a-z]*', data)
        if match_pairs and match_consec:
            count += 1
        
    print(count)
