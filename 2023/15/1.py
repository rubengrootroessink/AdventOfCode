def hasher(input_str):
    result = 0
    for c in input_str:
        result += ord(c)
        result *= 17
        result = result % 256
    return result

with open('input.txt') as f:
    data = f.read()[:-1].split(',')

print(sum([hasher(x) for x in data]))
