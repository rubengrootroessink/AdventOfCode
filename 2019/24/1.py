from collections import defaultdict
import hashlib

def create_hash(bit_string):
    bit_string = bit_string + '0' * 7 # Make size 32
    byte_array = bytearray(int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8)) 
    hash_obj = hashlib.sha256()
    hash_obj.update(byte_array)
    return hash_obj.hexdigest()

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

board = defaultdict(int)
bit_string = ''
for j, row in enumerate(data):
    for i, column in enumerate(row):
        if column == '#':
            board[(i, j)] = 1
            bit_string += '1'
        else:
            bit_string += '0'

seen = {create_hash(bit_string)}

while True:
    new_board = defaultdict(int)
    bit_string = ''

    for i in range(5):
        for j in range(5):
            ns = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            nns = len([board[x] for x in ns if board[x] == 1])
            if board[(i, j)] == 1 and nns != 1: # Bug dies
                bit_string += '0'
            elif board[(i, j)] == 1: # Bug survives
                new_board[(i, j)] = 1
                bit_string += '1'
            elif board[(i, j)] == 0 and nns in [1, 2]: # Empty space infested
                new_board[(i, j)] = 1
                bit_string += '1'
            else: # Empty space remains empty
                bit_string += '0'

    board = new_board

    hash_val = create_hash(bit_string)
    if hash_val in seen:
        bio_rate = 0
        for i in range(5):
            for j in range(5):
                if board[(i, j)] == 1:
                    bio_rate += 2**(i + j * 5)
        print(bio_rate)
        break
    else:
        seen.add(hash_val)
