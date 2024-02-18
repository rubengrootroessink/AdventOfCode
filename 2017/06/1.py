with open('input.txt') as f:
    blocks = [int(x) for x in f.read().split()]

length = len(blocks)

states = set()

i = 0
found = False
while not found:
    states.add(tuple(blocks))

    max_val = max(blocks)
    max_index = blocks.index(max_val)

    blocks[max_index] = 0
    index = (max_index+1)%length
    for val in range(max_val):
        blocks[index] = blocks[index] + 1
        index = (index+1)%length

    i += 1
    if tuple(blocks) in states:
        found = True

print(i)
