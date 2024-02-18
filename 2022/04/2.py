with open('input.txt', 'r') as f:
    data = [x.split('\n')[0].split(',') for x in f.readlines()]

result = 0
for item in data:
    fst, snd = item
    fst = [int(x) for x in fst.split('-')]
    snd = [int(x) for x in snd.split('-')]

    fst_set = set(range(fst[0], fst[-1]+1))
    snd_set = set(range(snd[0], snd[-1]+1))

    intersection = fst_set & snd_set
    if len(intersection) > 0:
        result += 1

print(result)
