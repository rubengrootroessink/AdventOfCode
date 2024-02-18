def eval(name, value_dict):
    values = value_dict[name]
    if type(values) == int:
        return values
    else:
        lhs, op, rhs = values.split(' ')
        if op == '+':
            return eval(lhs, value_dict) + eval(rhs, value_dict)
        elif op == '/':
            return eval(lhs, value_dict) // eval(rhs, value_dict)
        elif op == '-':
            return eval(lhs, value_dict) - eval(rhs, value_dict)
        elif op == '*':
            return eval(lhs, value_dict) * eval(rhs, value_dict)

with open('input.txt', 'r') as f:
    lines = [x.split('\n')[0].split(': ') for x in f.readlines()]

value_dict  = {}
for line in lines:
    try:
        value_dict[line[0]] = int(line[1])
    except Exception:
        value_dict[line[0]] = line[1]

print(eval('root', value_dict))
