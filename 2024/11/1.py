import math

def round(stones):
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        else:
            num_digits = int(math.log10(stone))+1
            if num_digits % 2 == 0:
                shift = 10**(num_digits // 2)
                num_1 = int(stone / shift)
                num_2 = stone - (num_1 * shift)
                result.append(num_1)
                result.append(num_2)
            else:
                result.append(stone*2024)
    return result

with open('input.txt') as f:
    stones = [int(x) for x in f.read().strip().split(' ')]

for i in range(0, 25):
    stones = round(stones)

print(len(stones))
