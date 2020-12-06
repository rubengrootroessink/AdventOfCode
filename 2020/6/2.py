count = 0
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    for line in data:
        lst = line.split('\n')
        lst = [set(x) for x in lst if not x == '']

        count += len(lst[0].intersection(*lst))
    
print(count)
