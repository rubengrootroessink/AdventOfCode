with open('input.txt', 'r') as f:
    data = list(f.read().split('\n')[0])
    result = sum([int(data[i]) for i in range(len(data)) if data[i] == data[(i+len(data)//2)%len(data)]])
    print(result)
