keypad = [
    [None, None, None, None, None, None, None],
    [None, None, None, 1, None, None, None],
    [None, None, 2, 3, 4, None, None],
    [None, 5, 6, 7, 8, 9, None],
    [None, None, 'A', 'B', 'C', None, None],
    [None, None, None, 'D', None, None, None],
    [None, None, None, None, None, None, None]
]
pos_x, pos_y = 3, 1

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [x.split('\n')[0] for x in lines]
    
    result = ""
    for line in lines:
        for char in line:
            if char == 'U':
                pos_x = pos_x - 1 if not keypad[pos_x-1][pos_y] is None else pos_x
            elif char == 'D':
                pos_x = pos_x + 1 if not keypad[pos_x+1][pos_y] is None else pos_x
            elif char == 'R':
                pos_y = pos_y + 1 if not keypad[pos_x][pos_y+1] is None else pos_y
            elif char == 'L':
                pos_y = pos_y - 1 if not keypad[pos_x][pos_y-1] is None else pos_y
        result += str(keypad[pos_x][pos_y])
    print(result)
