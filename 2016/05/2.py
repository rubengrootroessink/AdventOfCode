import hashlib

with open('input.txt', 'r') as f:
    door_id = f.read().split('\n')[0]
    
    result = [None] * 8
    index = 0
    while None in result:
        
        found = False
        while not found:
            temp_string = str(hashlib.md5(str(door_id + str(index)).encode()).hexdigest())
            if temp_string.startswith('00000'):
                first = temp_string[5]
                if first in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    found = True
                    if result[int(first)] is None:
                        result[int(first)] = temp_string[6]
            index += 1
    print("".join(result))
