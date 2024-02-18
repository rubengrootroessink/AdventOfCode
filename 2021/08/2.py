def check_sublist(str_1, str_2):
    return sum([1 for x in str_2 if x in str_1])

def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)

input_list = []
with open('input.txt') as file:
    input_list = [x for x in file.read().split('\n') if x != '']

result = 0
for item in input_list:
    map_dict = {}
    signals, output = item.split(' | ')
    signals = [''.join(sorted(x)) for x in signals.split(' ')]
    outputs = [''.join(sorted(x)) for x in output.split(' ')]

    for signal in signals:
        if len(signal) == 2:
            map_dict[1] = signal
        elif len(signal) == 3:
            map_dict[7] = signal
        elif len(signal) == 4:
            map_dict[4] = signal
        elif len(signal) == 7:
            map_dict[8] = signal

    for signal in signals:
        if len(signal) == 6:
            if check_sublist(map_dict[4], signal) == 4:
                map_dict[9] = signal
            elif check_sublist(map_dict[7], signal) == 3:
                map_dict[0] = signal
            else:
                map_dict[6] = signal
        elif len(signal) == 5:
            if check_sublist(map_dict[1], signal) == 2:
                map_dict[3] = signal
            elif check_sublist(map_dict[4], signal) == 3:
                map_dict[5] = signal
            else:
                map_dict[2] = signal
        
    result += int(''.join([str(find_key(map_dict, output)) for output in outputs]))

print(result)
