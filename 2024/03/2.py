import re

pattern = r'(mul\((\d{1,3}),(\d{1,3})\)|do(?:n\'t){0,1}\(\))'

with open('input.txt') as f:
    data = f.read()

result = 0

instrs = re.findall(pattern, data)

enabled = True
result = 0

for instr in instrs:
    if instr[0] == 'do()':
        enabled = True
    elif instr[0] == "don't()":
        enabled = False
    elif enabled:
        result += int(instr[1])*int(instr[2])

print(result)
