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

result = 0
for num in data:
    gen = num_gen(num)
    for i in range(0, 2000):
        curr = next(gen)
    result += curr

print(result)
