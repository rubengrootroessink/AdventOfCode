import heapq
from functools import reduce

def knot_hash(input_str):
    lengths = [ord(x) for x in input_str]
    iv = [17, 31, 73, 47, 23]
    lengths = lengths + iv

    list_nums = list(range(0, 256))
    curr_pos = 0
    skip_size = 0

    list_length = len(list_nums)
    for rnd in range(0, 64):
        for length in lengths:
            if curr_pos + length > list_length:
                sublist = list_nums[curr_pos:] + list_nums[:(curr_pos + length) % list_length]
                sublist = sublist[::-1]
                
                list_nums = sublist[list_length-curr_pos:] + list_nums[length-(list_length-curr_pos):curr_pos] + sublist[:list_length-curr_pos]
            else:
                list_nums = list_nums[:curr_pos] + list_nums[curr_pos:curr_pos + length][::-1] + list_nums[curr_pos+length:]

            curr_pos = (curr_pos + skip_size + length) % list_length
            skip_size += 1

    sparse_hash = list_nums
    hash_chunks = [sparse_hash[i:i+16] for i in range(0, list_length, 16)]

    dense_hash = [reduce(lambda i, j: i ^ j, chunk) for chunk in hash_chunks]
    hex_string = ''.join(["{:02x}".format(x) for x in dense_hash])
    binary_string = ''.join(["{:04b}".format(int(char, 16)) for char in hex_string])

    return binary_string

with open('input.txt') as f:
    ascii_string = f.read().strip()

matrix = []
for i in range(0, 128):
    hash_val = knot_hash(ascii_string + '-' + str(i))
    matrix.append(list(hash_val))

nr_regions = 0
while any(['1' in row for row in matrix]):
    nr_regions += 1

    start_val = None
    for y, row in enumerate(matrix):
        for x, column in enumerate(row):
            if column == '1' and start_val == None:
                start_val = (x, y)
                break
        if start_val != None:
            break

    heap = [start_val]
    while heap:
        curr_val = heapq.heappop(heap)

        matrix[curr_val[1]][curr_val[0]] = '0'

        neighbours = [
            (curr_val[0]-1, curr_val[1]),
            (curr_val[0]+1, curr_val[1]),
            (curr_val[0], curr_val[1]-1),
            (curr_val[0], curr_val[1]+1),
        ]

        neighbours = [(x, y) for (x, y) in neighbours if x in range(0, 128) and y in range(0, 128)]
        neighbours = [(x, y) for (x, y) in neighbours if matrix[y][x] == '1']
        
        for neighbour in neighbours:
            heapq.heappush(heap, neighbour)

print(nr_regions)
