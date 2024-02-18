import math

def get_fuel(mass):
    return math.floor(mass / 3) - 2

with open('input.txt') as f:
    masses = [int(x.strip()) for x in f.readlines()]

fuel = 0
for mass in masses:
    mass_fuel = mass

    finished = False
    while not finished:
        mass_fuel = get_fuel(mass_fuel)
        
        if mass_fuel <= 0:
            finished = True
        else:
            fuel += mass_fuel

print(fuel)
