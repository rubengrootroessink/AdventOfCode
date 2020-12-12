input = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input.append(int(data))

input = sorted(input)

result = []
for a in input:
    for b in input:
        if a + b == 2020:
            result.append(a*b)
            
print(list(set(result))[0])
