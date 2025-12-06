import math

with open('input.txt') as f:
    lines = [l[:-1][::-1] for l in f.readlines()]

num_entries = len(lines)-1

total = 0
last_operator = None
curr_nums = []
for i in range(len(lines[0])):
    num = ''.join([lines[j][i] for j in range(num_entries)])
    if lines[num_entries][i] in ['*', '+']:
        last_operator = lines[num_entries][i]

    if all(x == ' ' for x in num):
        total += math.prod(curr_nums) if last_operator == '*' else sum(curr_nums)
        curr_nums = []
    else:
        curr_nums.append(int(num))

total += math.prod(curr_nums) if last_operator == '*' else sum(curr_nums)

print(total)
