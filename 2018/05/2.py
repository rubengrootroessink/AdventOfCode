import re
import sys
import string

with open('input.txt') as f:
    polymer = f.read().strip()

pattern = r'(\w)\1+'

shortest = sys.maxsize
for char in string.ascii_lowercase:
    new_polymer = polymer.replace(char, '')
    new_polymer = new_polymer.replace(char.upper(), '')
    
    minimal = False
    while not minimal:
        matcher = re.finditer(pattern, new_polymer.lower())

        offset = 0
        changed = False
        for m in matcher:
            start_pos = m.start()-offset
            end_pos = m.end()-offset
            sub_item = new_polymer[start_pos:end_pos]
            for i in range(len(sub_item)-1):
                if (sub_item[i].islower() and sub_item[i+1].isupper()) or (sub_item[i+1].islower() and sub_item[i].isupper()):
                    new_polymer = new_polymer[:start_pos] + sub_item[:i] + sub_item[i+2:] + new_polymer[end_pos:]
                    offset += 2
                    changed = True
                    break

        if not changed:
            minimal = True

    shortest = min(shortest, len(new_polymer))

print(shortest)
