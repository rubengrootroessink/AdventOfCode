from collections import defaultdict
import math

def num_gen(start_number):
    secret_number = start_number
    while True:
        secret_number = ((secret_number * 64) ^ secret_number) % 16777216
        secret_number = (math.floor(secret_number / 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216

        yield secret_number

with open('input.txt') as f:
    data = [int(x) for x in f.readlines()]

occurrence_dict = defaultdict(list)

max_val = 0
for num in data:
    visited = set()

    prices = [num % 10]

    gen = num_gen(num)
    for i in range(0, 2000):
        curr = next(gen)

        prices.append(curr % 10)

        if len(prices) > 5:
            changes = tuple([y-x for x, y in zip(prices[:-2], prices[1:-1])])

            if not changes in visited:
                occurrence_dict[changes].append(prices[-2])
                visited.add(changes)
                max_val = max(max_val, sum(occurrence_dict[changes]))

            prices = prices[1:]

print(max_val)
