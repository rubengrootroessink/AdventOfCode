import re

with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

pattern = r'(?!(.)\1\1)((.)(.)\3)'

count = 0
for line in data:
    supernet_seqs = [[y for y in x if y != ''] for x in re.findall(r'^(\w+)\[|\](\w+)\[|\](\w+)$', line)]
    supernet_seqs = [item for sublist in supernet_seqs for item in sublist]
    hypernet_seqs = re.findall(r'\[(\w+)\]', line)
   
    abas = []
    for item in supernet_seqs:
        pattern = r'((\w)\w\2)'
        sublists = [item[i:i+3] for i in range(0, len(item)-2)]
        matchers = [x for x in sublists if re.match(pattern, x)]
        matchers = [x for x in matchers if x[0] != x[1]]
        abas = abas + matchers

    abas = list(set(abas))

    matches = False
    for aba in abas:
        for seq in hypernet_seqs:
            if aba[1] + aba[0] + aba[1] in seq:
                matches = True

    if matches:
        count += 1

print(count)
