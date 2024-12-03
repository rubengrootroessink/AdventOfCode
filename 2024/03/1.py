import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

with open('input.txt') as f:
    data = f.readlines()

result = 0
for line in data:
    matches = re.findall(pattern, line)
    result += sum([(int(x) * int(y)) for (x, y) in matches])

print(result)
