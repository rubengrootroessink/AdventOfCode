from collections import deque

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

nr_cards = 10007
deck = deque(list(range(0, nr_cards)))

for instr in instrs:
    if instr.startswith('deal into new stack'):
        deck.reverse()
    elif instr.startswith('cut'):
        amount = int(instr.split(' ')[-1])
        if amount > 0:
            [deck.append(x) for x in [deck.popleft() for x in range(amount)]]
        else:
            [deck.appendleft(x) for x in [deck.pop() for x in range(abs(amount))]]

    elif instr.startswith('deal with increment'):
        increment = int(instr.split(' ')[-1])
        tmp_dict = {}
        index = 0
        while len(deck) > 0:
            val = deck.popleft()
            tmp_dict[index] = val
            index = (index + increment) % nr_cards

        deck = deque([v for (k, v) in sorted(tmp_dict.items(), key=lambda x: x[0])])

print(deck.index(2019))
