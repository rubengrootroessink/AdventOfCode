with open('input.txt') as f:
    freq_changes = [x.strip() for x in f.readlines()]

print(sum([0-int(x[1:]) if x[0] == '-' else int(x[1:]) for x in freq_changes]))
