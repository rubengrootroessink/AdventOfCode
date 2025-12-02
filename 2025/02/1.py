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
while last_num == None or last_num < max_num:
    next_num = int(str(i) + str(i))
    if any(next_num in r for r in ranges):
        count += next_num
    last_num = next_num
    i += 1

print(count)
