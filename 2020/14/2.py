import itertools

def get_addresses(address):
    result = []
    Xs = address.count('X')    
    lst = list(itertools.product([0, 1], repeat=Xs))
    lst = [[str(x) for x in list(elem)] for elem in lst]

    for item in lst:
        temp = address
        for elem in item:
            temp = temp.replace('X', elem, 1)
        result.append(temp)
    
    return result

with open('input.txt', 'r') as file:
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    
    memory = {}
    for line in file.readlines():
        if line.startswith('mask'):
            mask = line.split(' = ')[1].split('\n')[0]
        elif line.startswith('mem'):
            temp = line.split(' = ')
            address = str(bin(int(temp[0].split('mem[')[1].split(']')[0])))[2:]
            address = (36 - len(address)) * '0' + address
            value = int(temp[1])
            
            masked_val = "".join([mask[i] if mask[i] == 'X' else address[i] if mask[i] == '0' else '1' for i in range(len(mask))])
            
            addresses = get_addresses(masked_val)
            for i, address in enumerate(addresses):
                memory[int(address, 2)] = value

    result = 0
    for key, value in memory.items():
        result += value
            
    print(result)
