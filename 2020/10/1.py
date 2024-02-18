with open('input.txt', 'r') as file:
    numbers = []
    for i, line in enumerate(file.readlines()):
        data = line.split("\n")[0]
        numbers.append(int(data))

    numbers = sorted(numbers)
    
    jumps_1 = 0
    jumps_2 = 0
    jumps_3 = 1 # Last jump
    
    prev_num = 0
    for nr in numbers:
        num = nr - prev_num
        if num == 1:
            jumps_1 += 1
        elif num == 2:
            jumps_2 += 1
        elif num == 3:
            jumps_3 += 1
        prev_num = nr
           
    print(jumps_3 * jumps_1)
