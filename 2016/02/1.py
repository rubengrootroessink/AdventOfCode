keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pos_x, pos_y = 1, 1

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [x.split('\n')[0] for x in lines]
    
    result = ""
    for line in lines:
        for char in line:
            if char == 'U':
                pos_x = max(0, pos_x - 1)
            elif char == 'D':
                pos_x = min(2, pos_x + 1)
            elif char == 'R':
                pos_y = min(2, pos_y + 1)
            elif char == 'L':
                pos_y = max(0, pos_y - 1)
        result += str(keypad[pos_x][pos_y])
    print(result)
