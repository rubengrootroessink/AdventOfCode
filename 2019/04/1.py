# Inspired by others
from collections import Counter

with open('input.txt') as f:
    low, high = [int(x) for x in f.read().strip().split('-')]

count = 0
for num in range(low, high+1):
    text = str(num)
    
    if text == ''.join(sorted(text)):
        c = set(Counter(text).values())
        if bool(c & {2, 3, 4, 5, 6}):
            count += 1

print(count)
