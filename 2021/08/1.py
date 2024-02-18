input_list = []
with open('input.txt') as file:
    input_list = [x.split(' | ')[1].split(' ') for x in file.read().split('\n') if x != '']

count = sum([1 for item in input_list for elem in item if len(elem) in [2, 3, 4, 7]])
print(count)

