with open('input.txt', 'r') as file:
    data = [int(x) for x in file.read().split(',')]
    
    data_dict = {}
    for i, item in enumerate(data[:len(data)-1]):
        data_dict[item] = i
        
    prev_num = data[-1]
    curr_index = len(data)

    while curr_index < 30000000:
        if prev_num not in data_dict.keys():
            data_dict[prev_num] = curr_index - 1
            prev_num = 0
        else:
            old_val = data_dict[prev_num]
            data_dict[prev_num] = curr_index - 1
            prev_num = (curr_index - 1) - old_val
        curr_index += 1
    print(prev_num)
