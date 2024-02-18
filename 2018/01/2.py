with open('input.txt') as f:
    freq_changes = [x.strip() for x in f.readlines()]
    freq_changes = [0-int(x[1:]) if x[0] == '-' else int(x[1:]) for x in freq_changes]

prev_freqs = {0}
index = 0
freq = 0
found = False
while not found:
    freq += freq_changes[index]

    if freq in prev_freqs:
        print(freq)
        found = True
    else:
        prev_freqs.add(freq)

    index = (index + 1) % len(freq_changes)
