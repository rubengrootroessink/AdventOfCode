import heapq

with open('input.txt') as f:
    data = [(int(x), i%2==0) for i, x in enumerate(f.read().strip())]

final_index = 0

id_num = 0
new_data = []
for val, filled in data:
    if filled:
        new_data.append((val, id_num))
        id_num += 1
        final_index += val
    else:
        new_data.append((val, False))

data = new_data

checksum = 0
checksum_index = 0
data_index = 0
back_index = len(data)-1
if not data[back_index][1]:
    back_index -= 1

curr_vals = []
while checksum_index < final_index:
    length, id_num = data[data_index]

    if type(id_num) == int:

        if checksum_index + length > final_index:
            for i, v in enumerate(curr_vals):
                checksum += (checksum_index+i)*v
            checksum_index == final_index
            break

        for j in range(length):
            checksum += (checksum_index+j) * id_num
        checksum_index += length
    else:
        for j in range(length):
            if len(curr_vals) == 0:
                curr_vals = [data[back_index][1]]*data[back_index][0]
                back_index -= 2

                if back_index < data_index:
                    break

            checksum += (checksum_index + j) * heapq.heappop(curr_vals)
        checksum_index += length

    data_index += 1

print(checksum)
