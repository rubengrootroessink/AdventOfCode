import hashlib

with open('input.txt', 'r') as f:
    integer = 1
    value = f.read().split('\n')[0]
    found = False
    while not found:
        curr_string = value + str(integer)
        integer += 1
        result = hashlib.md5(curr_string.encode())
        md5_hash = result.hexdigest()
        if md5_hash[0:6] == '000000':
             found = True
             print(curr_string, md5_hash)

