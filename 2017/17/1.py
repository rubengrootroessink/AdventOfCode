from collections import deque

with open('input.txt') as f:
    step_size = int(f.read().strip())

queue = deque([0])

for i in range(1, 2018):
    queue.rotate(-step_size)
    queue.append(i)

print(queue.popleft())
