import math

def get_fuel(mass):
    return math.floor(mass / 3) - 2

with open('input.txt') as f:
    masses = [int(x.strip()) for x in f.readlines()]

fuel = sum([get_fuel(x) for x in masses])

print(fuel)
