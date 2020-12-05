with open('input.txt', 'r') as f:
    data = f.read()
    up = sum([1 for x in data if x == '('])
    down = sum([1 for x in data if x == ')'])
    print(up - down)
