import re

with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0]
    lt = re.findall('-?\d+', data)
    print(sum([int(x) for x in lt]))
