from collections import defaultdict

def ret_val():
    return '.'

with open('input.txt') as f:
    initial_state, changes = f.read().strip().split('\n\n')
    initial_state = list(initial_state.split('state: ')[1])
    changes = [tuple(x.split(' => ')) for x in changes.split('\n')]

change_dict = defaultdict(ret_val)
for c, r in changes:
    change_dict[c] = r

pots = defaultdict(ret_val)
for i, val in enumerate(initial_state):
    pots[i] = val

i = 0
nr_seq = 0
prev = 0
diff = 0
while nr_seq < 100:
    new_pots = defaultdict(ret_val)
    
    f_hashtag = min([k for k, v in pots.items() if v == '#'])-4 if i > 0 else 0
    l_hashtag = max([k for k, v in pots.items() if v == '#'])+4

    for j in range(f_hashtag, l_hashtag):
        tmp_string = ''.join([pots[k+j] for k in range(-2, 3)])
        new_val = change_dict[tmp_string]

        new_pots[j] = new_val

    if len(pots) == len(new_pots)+4:
        count += 1
    
    pots = new_pots

    i += 1

    count = 0
    for key, value in pots.items():
        if value == '#':
            count += key

    if count - prev == diff:
        nr_seq += 1
    else:
        nr_seq = 0

    diff = count - prev
    prev = count

print((50000000000-i)*diff+prev)
