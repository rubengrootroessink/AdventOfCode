import hashlib

with open('input.txt', 'r') as f:
    door_id = f.read().split('\n')[0]
    
    result = ''
    index = 0
    while len(result) != 8:
        
        found = False
        while not found:
            temp_string = str(hashlib.md5(str(door_id + str(index)).encode()).hexdigest())
            if temp_string.startswith('00000'):
                found = True
                result += temp_string[5]

            index += 1
    print(result)
