rules = {}
template = ''
uniq = []
with open('input.txt') as file:
    template, raw_rules = file.read().split('\n\n')
    raw_rules = [x.split(' -> ') for x in raw_rules.split('\n') if x != '']
    for rule in raw_rules:
        rules[rule[0]] = rule[1]
        for char in rule[0]:
            uniq.append(char)
        for char in rule[1]:
            uniq.append(char)

polymer = {}
pairs = list(zip(template[0:-1], template[1:]))
pairs = [str(''.join(x)) for x in pairs]
for item in pairs:
    if item in polymer.keys():
        polymer[item] += 1
    else:
        polymer[item] = 1

uniq = list(set(uniq))

for step in range(0, 40):
    new_polymer = {}
    for key, value in polymer.items():
        f_key = key[0] + rules[key]
        if f_key in new_polymer.keys():
            new_polymer[f_key] += value
        else:
            new_polymer[f_key] = value
        s_key = rules[key] + key[1]
        if s_key in new_polymer.keys():
            new_polymer[s_key] += value
        else:
            new_polymer[s_key] = value
    polymer = new_polymer

char_counts = {}
for char in uniq:
    char_result = 0
    for key, value in new_polymer.items():
        if key[0] == char:
            char_result += value
        if key[1] == char:
            char_result += value
    char_counts[char] = char_result

for char, value in char_counts.items():
    char_counts[char] = value // 2

char_counts[template[0]] += 1
char_counts[template[-1]] += 1

print(max(char_counts.values()) - min(char_counts.values()))
