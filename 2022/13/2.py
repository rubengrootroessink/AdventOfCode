import json
import functools

def check(left, right):
    for i, item in enumerate(left):
        if i >= len(right):
            return False
        elif type(item) == int and type(right[i]) == int:
            if item < right[i]:
                return True
            elif item > right[i]:
                return False
        elif type(item) == list and type(right[i]) == list:
            if check(item, right[i]) == 'Equal':
                continue
            elif check(item, right[i]):
                return True
            elif not check(item, right[i]):
                return False
        elif type(item) == int and type(right[i]) == list:
            val = check([item], right[i])
            if val == 'Equal':
                continue
            else:
                return val
        elif type(item) == list and type(right[i]) == int:
            val = check(item, [right[i]])
            if val == 'Equal':
                continue
            else:
                return val

    if len(left) < len(right):
        return True

    return 'Equal'

with open('input.txt') as f:
    data = f.read()[:-1].split('\n\n')

packet_list = [[[2]], [[6]]]
for i, item in enumerate(data):
    left, right = [json.loads(x) for x in item.split('\n')]
    packet_list.append(left)
    packet_list.append(right)

packet_list.sort(key=functools.cmp_to_key(lambda a, b: -1 if check(a, b) else 1))

print((packet_list.index([[2]])+1) * (packet_list.index([[6]])+1))
'''
#right_order = check(left, right)

    if right_order:
        result_list.append(i+1)

print(sum(result_list))
'''
