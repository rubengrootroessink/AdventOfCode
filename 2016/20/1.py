with open('input.txt') as f:
    ip_ranges = [x.strip() for x in f.readlines()]

ranges = []
for rng in ip_ranges:
    s, f = [int(x) for x in rng.split('-')]
    ranges.append(range(s, f+1))

ranges = sorted(ranges, key=lambda x: x[0])
l_elems = [x[-1]+1 for x in ranges]

for elem in l_elems:

    found = True
    for rng in ranges:
        if elem in rng:
            found = False

    if found:
        print(elem)
        break
