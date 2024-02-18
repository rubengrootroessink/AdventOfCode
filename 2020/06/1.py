count = 0
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    for line in data:
        count += len(set(line.replace('\n', '')))
    
print(count)
