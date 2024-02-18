with open('input.txt') as f:
    data = [[int(y) for y in x.split('\n')[0].split()] for x in f.readlines()]

result = 0
for row in data:
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            highest = max(row[i], row[j])
            lowest = min(row[i], row[j])

            if highest % lowest == 0:
                result += highest // lowest

print(result)
