import copy

def mix(lines, length, decrypt_key=1, mix_times=1):
    linked_list = {}
    zero_value = None
    for i, line in enumerate(lines):
        linked_list[(i, line*decrypt_key)] = ((i-1)%length, lines[i-1]*decrypt_key), ((i+1)%length, lines[(i+1)%length]*decrypt_key)
        if line == 0:
            zero_value = (i, line*decrypt_key)

    for _ in range(mix_times):
        for i, line in enumerate(lines):
            decrypt_line = line*decrypt_key

            curr_elem = linked_list[(i, decrypt_line)]
            prev_elem = linked_list[curr_elem[0]]
            next_elem = linked_list[curr_elem[1]]

            mod_line = decrypt_line % (length-1)
            new_right = linked_list[curr_elem[1]]
            for j in range(1, mod_line + 1):
                new_right = linked_list[new_right[1]]
            new_left = linked_list[new_right[0]]

            if mod_line == 1:
                linked_list[curr_elem[0]] = (prev_elem[0], curr_elem[1])
                linked_list[curr_elem[1]] = (curr_elem[0], (i, decrypt_line))
                linked_list[(i, decrypt_line)] = (curr_elem[1], next_elem[1])
                linked_list[next_elem[1]] = ((i, decrypt_line), new_right[1])
            elif mod_line == length-2:
                linked_list[new_right[0]] = (new_left[0], (i, decrypt_line))
                linked_list[curr_elem[0]] = ((i, decrypt_line), curr_elem[1])
                linked_list[(i, decrypt_line)] = (new_right[0], curr_elem[0])
                linked_list[curr_elem[1]] = (curr_elem[0], next_elem[1])
            elif mod_line > 1:
                linked_list[curr_elem[0]] = (prev_elem[0], curr_elem[1])
                linked_list[curr_elem[1]] = (curr_elem[0], next_elem[1])
                linked_list[new_right[0]] = (new_left[0], (i, decrypt_line))
                linked_list[(i, decrypt_line)] = (new_right[0], new_left[1])
                linked_list[new_left[1]] = ((i, decrypt_line), new_right[1])

    return zero_value, linked_list

with open('input.txt', 'r') as f:
    lines = [int(x.split('\n')[0]) for x in f.readlines()]

length = len(lines)

zero_value, linked_list = mix(lines, length, decrypt_key=811589153, mix_times=10)

new_value = zero_value
result = []
for i in range(0, 1000 % length):
    new_value = linked_list[new_value][1]
result.append(new_value[1])

for i in range(0, 1000 % length):
    new_value = linked_list[new_value][1]
result.append(new_value[1])

for i in range(0, 1000 % length):
    new_value = linked_list[new_value][1]
result.append(new_value[1])

print(sum(result))
