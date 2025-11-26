visited_patterns = {}

def recurse(pattern, available):
    if pattern in visited_patterns.keys():
        return visited_patterns[pattern]

    if pattern == '':
        return 1
    else:
        options = [a for a in available if pattern[0:len(a)] == a]
        if len(options) == 0:
            visited_patterns[pattern] = 0
            return 0
        else:
            answer = sum([recurse(pattern[len(a):], available) for a in options])
            visited_patterns[pattern] = answer
            return answer

with open('input.txt') as f:
    available, desired = f.read().strip().split('\n\n')

available = available.split(', ')
desired = desired.split('\n')

count = 0
for pattern in desired:
    count += recurse(pattern, available)

print(count)
