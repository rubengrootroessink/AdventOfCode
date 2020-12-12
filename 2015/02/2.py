with open('input.txt', 'r') as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        data = line.split('\n')[0].split('x')
        data = [int(x) for x in data]
        
        length, width, height = data[0], data[1], data[2]
        sorted_data = sorted(data)
        
        length = 2 * (sorted_data[0] + sorted_data[1])
        bow = sorted_data[0] * sorted_data[1] * sorted_data[2]
        total += length + bow

    print(total)
