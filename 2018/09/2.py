# Inspired by others

from collections import deque
import re

pattern = r'(\d+) players; last marble is worth (\d+) points'

with open('input.txt') as f:
    num_elves, num_marbles = [int(x) for x in re.match(pattern, f.read().strip()).groups()]

num_marbles = 100*num_marbles

elf_scores = {}

circle = deque([0])
for i in range(1, num_marbles):
    if i % 23 != 0:
        circle.rotate(-1)
        circle.append(i)
    else:
        circle.rotate(7)
        value = circle.pop()
        elf_num = i % num_elves
        if i % num_elves in elf_scores.keys():
            elf_scores[elf_num] += i + value
        else:
            elf_scores[elf_num] = i + value
        circle.rotate(-1)

print(max(elf_scores.values()))
