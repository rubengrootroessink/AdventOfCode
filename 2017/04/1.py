with open('input.txt') as f:
    data = [x.split('\n')[0].split(' ') for x in f.readlines()]

result = 0
for line in data:
    if len(line) == len(set(line)):
        result += 1

print(result)
