paths = {}
def path(start, end, numbers):
    k = (len(numbers), start)
    if k in paths:
        return paths[k]
    
    ways = 0
    if end - start <= 3:
        ways += 1
    if numbers == []:
        return ways
    if numbers[0] - start <= 3:
        ways += path(numbers[0], end, numbers[1:])
    ways += path(start, end, numbers[1:])
    paths[k] = ways
    return ways

with open('input.txt', 'r') as file:
    numbers = []
    for i, line in enumerate(file.readlines()):
        data = line.split("\n")[0]
        numbers.append(int(data))

    numbers = sorted(numbers)
    print(path(0, max(numbers) + 3, numbers))
