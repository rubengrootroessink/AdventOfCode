from collections import defaultdict
import math

def round(stone_dict):
    result_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        if stone == 0:
            result_dict[1] += count
        else:
            num_digits = int(math.log10(stone))+1
            if num_digits % 2 == 0:
                shift = 10**(num_digits // 2)
                num_1 = int(stone / shift)
                num_2 = stone - (num_1 * shift)
                result_dict[num_1] += count
                result_dict[num_2] += count
            else:
                result_dict[stone*2024] += count

    return result_dict

with open('input.txt') as f:
    stones = [int(x) for x in f.read().strip().split(' ')]

stone_dict = defaultdict(int)
for stone in stones:
    stone_dict[stone] += 1

for i in range(0, 75):
    stone_dict = round(stone_dict)

result = 0
for key, value in stone_dict.items():
    result += value

print(result)
