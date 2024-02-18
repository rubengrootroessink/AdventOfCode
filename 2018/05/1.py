import re

with open('input.txt') as f:
    polymer = f.read().strip()

pattern = r'(\w)\1+'

minimal = False
while not minimal:
    matcher = re.finditer(pattern, polymer.lower())

    offset = 0
    changed = False
    for m in matcher:
        start_pos = m.start()-offset
        end_pos = m.end()-offset
        sub_item = polymer[start_pos:end_pos]
        for i in range(len(sub_item)-1):
            if (sub_item[i].islower() and sub_item[i+1].isupper()) or (sub_item[i+1].islower() and sub_item[i].isupper()):
                polymer = polymer[:start_pos] + sub_item[:i] + sub_item[i+2:] + polymer[end_pos:]
                offset += 2
                changed = True
                break

    if not changed:
        minimal = True

print(len(polymer))
