import re

with open('input.txt') as f:
    logs = sorted([x.strip() for x in f.readlines()])

guard_dict = {}

active_guard = None
awake = True
curr_min = 0

log_pattern = r'^\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\] (.*)$'
message_pattern = r'^Guard #(\d+) begins shift$'

for log in logs:
    y, m, d, h, m, message = re.match(log_pattern, log).groups()
    m = int(m)

    guard_message = re.match(message_pattern, message)
    if guard_message:
        active_guard = int(guard_message.groups()[0])
        if not active_guard in guard_dict.keys():
            guard_dict[active_guard] = []

    elif message == 'falls asleep':
        awake = False
        curr_min = m

    elif message == 'wakes up':
        awake = True
        guard_dict[active_guard].append(range(curr_min, m))

guards = []
for guard in guard_dict.keys():
    minute_dict = {}
    for i in range(60):
        count = 0
        for rng in guard_dict[guard]:
            if i in rng:
                count += 1
        minute_dict[i] = count
    most_common_min = sorted(minute_dict.items(), key=lambda x: -x[1])[0]
    guards.append((guard, most_common_min[0], most_common_min[1]))

most_sleepy_guard = sorted(guards, key=lambda x: -x[2])[0]
print(most_sleepy_guard[0] * most_sleepy_guard[1])
