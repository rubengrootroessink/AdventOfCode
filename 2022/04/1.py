with open('input.txt', 'r') as f:
    data = [x.split('\n')[0].split(',') for x in f.readlines()]

result = 0
for item in data:
    fst, snd = item
    fst = [int(x) for x in fst.split('-')]
    snd = [int(x) for x in snd.split('-')]

    if fst[0] >= snd[0] and fst[-1] <= snd[-1]:
        result += 1
    elif fst[0] <= snd[0] and fst[-1] >= snd[-1]:
        result += 1

print(result)
