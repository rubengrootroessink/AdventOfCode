with open('input.txt', 'r') as f:
    data = f.read()
    curr_floor = 0
    for i, elem in enumerate(data):
        if elem == '(':
            curr_floor += 1
        elif elem == ')':
            curr_floor -= 1
        if curr_floor == -1:
            print(i)
