max_num = 0
ranges = []

with open('input.txt') as f:
    for x in f.read().strip().split(','):
        l, h = [int(y) for y in x.split('-')]
        ranges.append(range(l, h+1))
        max_num = max(max_num, h)

i = 1
count = 0
last_num = None
size_last_num = len(str(max_num))
matches = set()
while True:
    next_num_str = str(i) + str(i)
    next_num = int(next_num_str)
    if len(next_num_str) > size_last_num:
        break
    else:
        while int(next_num) < max_num:
            if any(next_num in r for r in ranges):
                matches.add(next_num)
            next_num_str += str(i)
            next_num = int(next_num_str)
    i += 1

print(sum(matches))
