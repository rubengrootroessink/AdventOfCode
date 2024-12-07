from itertools import product

with open('input.txt') as f:
    lines = [[int(y) for y in x.strip().replace(':', '').split(' ')] for x in f.readlines()]

cal_result = 0
for line in lines:
    result = line[0]
    values = line[1:]
    options = product(['*', '+'], repeat=len(values)-1)

    matches = False
    for option in options:
        ops = ['*'] + list(option)
        
        tmp_result = 1
        for i, val in enumerate(values):
            if ops[i] == '*':
                tmp_result *= val
            elif ops[i] == '+':
                tmp_result += val
            
            if tmp_result > result:
                break

        if tmp_result == result:
            matches = True
            break

    if matches:
        cal_result += result

print(cal_result)
