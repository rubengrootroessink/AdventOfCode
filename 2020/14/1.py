with open('input.txt', 'r') as file:
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    
    memory = {}
    for line in file.readlines():
        if line.startswith('mask'):
            mask = line.split(' = ')[1].split('\n')[0]
        elif line.startswith('mem'):
            temp = line.split(' = ')
            address = int(temp[0].split('mem[')[1].split(']')[0])
            value = str(bin(int(temp[1])))[2:]
            value = (36 - len(value)) * '0' + value
            
            masked_val = int("".join([mask[i] if mask[i] != 'X' else value[i] for i in range(len(mask))]), 2)
            
            memory[address] = masked_val
     
    result = 0
    for key, value in memory.items():
        result += value
            
    print(result)
