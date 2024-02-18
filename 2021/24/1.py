correct_vals = []

def evaluate(lines, in_data):
    globals().update([['w', 0]])
    globals().update([['x', 0]])
    globals().update([['y', 0]])
    globals().update([['z', 0]])

    user_input = in_data
    for line in lines:
        op = line[0]
        lhs = line[1]
        if op == 'inp':
            in_val = int(user_input[0])
            user_input = user_input[1:]
            globals().update([[lhs, in_val]])
        else:
            f_value = globals().get(lhs, None)
            rhs = line[2]
            if rhs.isnumeric() or (rhs[0] == '-' and rhs[1:].isnumeric()):
                s_value = int(rhs)
            else:
                s_value = globals().get(rhs, None)

            value = 0
            if op == 'add':
                value = f_value + s_value
            elif op == 'mul':
                value = f_value * s_value
            elif op == 'div':
                value = f_value // s_value
            elif op == 'mod':
                value = f_value % s_value
            elif op == 'eql':
                value = 1 if f_value == s_value else 0
            globals().update([[lhs, value]])

    w = globals().get('w', None)
    x = globals().get('x', None)
    y = globals().get('y', None)
    z = globals().get('z', None)
    return  w, x, y, z

def find_input(in_val, i, vals, path, add_x, add_y, divs, data):
    if i == 13:
        if evaluate(data, [str(x) for x in path])[3] == 0:
            correct_vals.append(''.join([str(x) for x in path]))
        return True

    if divs[i] == 26:
        if in_val - add_x[i] != vals[-1]:
            return False
        for n_val in range(9, 0, -1):
            find_input(n_val, i+1, vals[:-1], path + [n_val], add_x, add_y, divs, data)
    else:
        for n_val in range(9, 0, -1):
            find_input(n_val, i+1, vals + [in_val + add_y[i]], path + [n_val], add_x, add_y, divs, data)

blocks = []
with open('input.txt') as f:
    data = f.read().split('\ninp w\n')
    data[0] = data[0].split('inp w\n')[1]
    data[-1] = data[-1][:-1]
    blocks = data

overlap = [list(sublist) for sublist in list(zip(*[block.split('\n') for block in blocks]))]
overlap = [item[0] if all([item[0] == elem for elem in item]) else item for item in overlap]

divs = [int(x.split('div z ')[1]) for x in overlap[3]]
add_x = [int(x.split('add x ')[1]) for x in overlap[4]]
add_y = [int(x.split('add y ')[1]) for x in overlap[14]]

data = []
with open('input.txt') as f:
    data = [x.split('\n')[0].split(' ') for x in f.readlines()]

for in_val in range(9, 0, -1):
    find_input(in_val, 0, [], [in_val], add_x, add_y, divs, data)

print(correct_vals[0])

# With help from: https://notes.dt.in.th/20211224T121217Z7595
