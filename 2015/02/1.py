with open('input.txt', 'r') as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        data = line.split('\n')[0].split('x')
        data = [int(x) for x in data]
        
        length, width, height = data[0], data[1], data[2]
        sorted_data = sorted(data)
        
        minimum = sorted_data[0] * sorted_data[1]
        total += 2 * length * width + 2 * width * height + 2 * height * length + minimum

    print(total)
