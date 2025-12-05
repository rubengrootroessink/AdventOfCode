ranges = sorted([range(r[0], r[1]+1) for r in map(lambda x: tuple(map(int, x.split('-'))), open('input.txt').read().split('\n\n')[0].split('\n'))], key=lambda y: (y[0], y[-1]))

total = 0
end = ranges[0][0]
for r in ranges:
    if r[0] > end:
        total += r[-1] - r[0] + 1
    else:
        total += max(0, r[-1] - end)
    end = max(end, r[-1])

print(total)
