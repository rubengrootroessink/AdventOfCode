# Inspiration from others, cool problem!

with open('input.txt') as f:
    num_elves = int(f.read())

i = 1
while i*3 < num_elves:
    i *= 3

print(num_elves - i)
