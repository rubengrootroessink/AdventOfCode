import re
import heapq

with open('input.txt') as f:
    instrs = [x.split('\n')[0] for x in f.readlines()]

start_dict = {}

value_pattern = r'^value (\d+) goes to bot (\d+)$'
handover_pattern = r'^bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)$'
for instr in instrs:
    if instr.startswith('value'):
        value, bot = [int(x) for x in re.match(value_pattern, instr).groups()]
        if bot in start_dict.keys():
            start_dict[bot]['chips'].append(value)
        else:
            start_dict[bot] = {
                'chips': [value],
            }
    
    else:
        bot, rec_1, rec_val_1, rec_2, rec_val_2 = re.match(handover_pattern, instr).groups()
        bot, rec_val_1, rec_val_2 = [int(x) for x in [bot, rec_val_1, rec_val_2]]
        if bot in start_dict.keys():
            start_dict[bot]['low'] = (rec_1, rec_val_1)
            start_dict[bot]['high'] = (rec_2, rec_val_2)
        else:
            start_dict[bot] = {
                'chips': [],
                'low': (rec_1, rec_val_1),
                'high': (rec_2, rec_val_2),
            }

start_bot = None
for bot, val in start_dict.items():
    if len(val['chips']) == 2:
        start_bot = bot

output_dict = {}
heap = [start_bot]
while heap:
    curr_bot = heapq.heappop(heap)

    copy_dict = start_dict[curr_bot]
    chips = sorted(copy_dict['chips'])

    t1, r1 = copy_dict['low']
    t2, r2 = copy_dict['high']

    if len(chips) != 2:
        continue

    if t1 == 'bot':
        start_dict[r1]['chips'].append(chips[0])
        heapq.heappush(heap, r1)
    else:
        output_dict[r1] = chips[0]

    if t2 == 'bot':
        start_dict[r2]['chips'].append(chips[1])
        heapq.heappush(heap, r2)
    else:
        output_dict[r2] = chips[1]

    start_dict[curr_bot]['chips'] = []

print(output_dict[0]*output_dict[1]*output_dict[2])
