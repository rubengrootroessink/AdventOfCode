import collections

input_list = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        input_list.append(data)

def most_common(lst, o):
    c = collections.Counter(lst).most_common(2)
    return c[1-o][0] if c[0][1] > c[1][1] else str(o)

o_vals = c_vals = input_list

i = 0
o_found = c_found = False
while not o_found or not c_found:
    if len(o_vals) > 1:
        o_bits = [x[i] for x in o_vals]
        m = most_common(o_bits, 1)
        o_vals = [x for x in o_vals if x[i] == m]
    elif len(o_vals) == 1:
        o_found = True

    if len(c_vals) > 1:
        c_bits = [x[i] for x in c_vals]
        m = most_common(c_bits, 0)
        c_vals = [x for x in c_vals if x[i] == m]                     
    elif len(c_vals) == 1:
        c_found = True 
    
    i += 1

print(int(o_vals[0], 2) * int(c_vals[0], 2))
