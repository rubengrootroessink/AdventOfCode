from collections import Counter

with open('input.txt') as f:
    box_ids = [x.strip() for x in f.readlines()]

twos = 0
threes = 0

for box_id in box_ids:
    char_dict = dict(Counter(box_id))
    char_vals = set(char_dict.values())
    if 2 in char_vals:
        twos += 1
    if 3 in char_vals:
        threes += 1

print(twos * threes)
