with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

replace_dict = {
    'one': '1',
    'two': '2',
    'six': '6',
    'four': '4',
    'five': '5',
    'nine': '9',
    'three': '3',
    'seven': '7',
    'eight': '8',
}

result = 0
for line in data:
    integers = []

    for index in range(0, len(line)):
        if line[index].isdigit():
            integers.append(line[index])
        else:
            for key, value in replace_dict.items():
                if index + len(key) > len(line):
                    pass
                elif line[index:index+len(key)] == key:
                    integers.append(value)

    f, s = integers[0], integers[-1]
    result += int(f + s)

print(result)
