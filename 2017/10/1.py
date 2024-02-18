with open('input.txt') as f:
    lengths = [int(x) for x in f.read().split(',')]

list_nums = list(range(0, 256))
curr_pos = 0
skip_size = 0

list_length = len(list_nums)

for length in lengths:

    if curr_pos + length > list_length:
        sublist = list_nums[curr_pos:] + list_nums[:(curr_pos + length) % list_length]
        sublist = sublist[::-1]
                
        list_nums = sublist[list_length-curr_pos:] + list_nums[length-(list_length-curr_pos):curr_pos] + sublist[:list_length-curr_pos]
    else:
        list_nums = list_nums[:curr_pos] + list_nums[curr_pos:curr_pos + length][::-1] + list_nums[curr_pos+length:]

    curr_pos = (curr_pos + skip_size + length) % list_length
    skip_size += 1

print(list_nums[0] * list_nums[1])
