locations = []
with open('input.txt', 'r') as f:
    santa_x, santa_y = 0, 0
    r_santa_x, r_santa_y = 0, 0
    for i, char in enumerate(f.read()):
        x, y = 0, 0
        if i % 2 == 0:
    	    x, y = santa_x, santa_y
        else:
    	    x, y = r_santa_x, r_santa_y

        if char == '^':
            x += 1
        elif char == 'v':
            x -= 1
        elif char == '<':
            y -= 1
        elif char == '>':
            y += 1
        locations.append((x, y))

        if i % 2 == 0:
            santa_x, santa_y = x, y
        else:
            r_santa_x, r_santa_y = x, y

print(len(set(locations)))
