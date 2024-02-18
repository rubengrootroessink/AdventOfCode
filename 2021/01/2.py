input_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input_list.append(int(data))

list_1 = input_list[:-3]
list_2 = input_list[3:]

print(len([list_2[i] - list_1[i] for i in range(len(list_1)) if list_2[i] - list_1[i] > 0]))
