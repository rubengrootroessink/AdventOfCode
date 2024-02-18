with open('input.txt') as file:
    input_list = [int(x) for x in file.read().split(',')]

fish_dickt = {}
for item in input_list:
    fish_dickt[item] = fish_dickt[item] + 1 if item in fish_dickt.keys() else 1

days = range(0, 80)
for day in days:
    fish_dickt = {key - 1: value for key, value in fish_dickt.items()}
    if -1 in fish_dickt.keys():
        new_gen = fish_dickt[-1]
        fish_dickt[6] = fish_dickt[6] + new_gen if 6 in fish_dickt.keys() else new_gen
        fish_dickt[8] = fish_dickt[8] + new_gen if 8 in fish_dickt.keys() else new_gen
        fish_dickt.pop(-1)

print(sum([value for key, value in fish_dickt.items()]))
