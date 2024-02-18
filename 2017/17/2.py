# Ugly bruteforce
from collections import deque

with open('input.txt') as f:
    step_size = int(f.read().strip())

queue = deque([0])

for i in range(1, 50000001):
    queue.rotate(-step_size)
    queue.append(i)

val = queue.popleft()
while val != 0:
    val = queue.popleft()

print(queue.popleft())
