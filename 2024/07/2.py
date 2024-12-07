import math

with open('input.txt') as f:
    lines = [[int(y) for y in x.strip().replace(':', '').split(' ')] for x in f.readlines()]

def rec(final_val, curr_val, vals):
    if curr_val > final_val:
        return False
    elif final_val == curr_val and vals == []:
        return True
    elif vals == []:
        return False
    else:
        new_vals = []
        new_vals.append(curr_val + vals[0])
        new_vals.append(curr_val * vals[0])
        new_vals.append(curr_val * 10**int(math.log10(vals[0]) + 1) + vals[0])
        return any([rec(final_val, new_val, vals[1:]) for new_val in new_vals])

cal_result = 0
for line in lines:
    result = line[0]
    values = line[1:]

    if rec(result, 0, values):
        cal_result += result

print(cal_result)
