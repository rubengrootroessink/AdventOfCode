input_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input_list.append(data)

transposed = list(zip(*input_list))
transposed = [list(sublist) for sublist in transposed]
gamma = ''.join([max(set(x), key=x.count) for x in transposed])

print(int(gamma, 2) * (int(gamma, 2) ^ int("1"*len(input_list[0]), 2)))
