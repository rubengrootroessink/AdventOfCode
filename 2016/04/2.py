from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [x.split(']\n')[0].split('[') for x in lines]
    
    sum_matching = 0
    
    real_rooms = []
    for line in lines:
        room_id, sec_id = line[0].rsplit('-', 1)
        checksum = line[1]
        sec_id = int(sec_id)
        string = room_id.replace('-', '')
        string = reduce(lambda x, y: x + y, sorted(string))
        
        result = {}
        for c in string:
            if c in result.keys():
                result[c] += 1
            else:
                result[c] = 1

        sorted_list = sorted(result.items(), key=lambda x: (-x[1], x[0]))
        stringified = "".join([y[0] for y in sorted_list])
        if stringified[:len(checksum)] == checksum:
            real_rooms.append([room_id, sec_id])
            
    for line, sec_id in real_rooms:
        rotations = sec_id % 26
        result = ''
        for c in line:
            if c != '-':
                result += chr(((ord(c) - 97 + rotations) % 26) + 97)
            else:
                result += ' '
        
        if 'northpole object' in result:
            print(sec_id)
