input = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input.append(int(data))

input = sorted(input)

result = []
for a in input:
    for b in input:
        for c in input:
            if a + b + c == 2020:
                result.append(a * b * c)
            
print(list(set(result))[0])
