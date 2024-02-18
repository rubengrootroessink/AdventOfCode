locations = []
with open('input.txt', 'r') as f:
    x, y = 0, 0
    for char in f.read():
        if char == '^':
            x += 1
        elif char == 'v':
            x -= 1
        elif char == '<':
            y -= 1
        elif char == '>':
            y += 1
        locations.append((x, y))

print(len(set(locations)))
