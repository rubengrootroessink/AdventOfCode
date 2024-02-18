import copy

def build_tree(value, value_dict):
    result_dict = {}
    item = value_dict[value]
    if type(item) == int:
        result_dict[value] = {
            'value': item,
        }
    else:
        lhs, op, rhs = item.split(' ')
        result_dict[value] = {
            'left': lhs,
            'op': op,
            'right': rhs,
        }

        left = build_tree(lhs, value_dict)
        for k, v in left.items():
            result_dict[k] = v
            if not 'parent' in result_dict[k].keys():
                result_dict[k]['parent'] = value

        right = build_tree(rhs, value_dict)
        for k, v in right.items():
            result_dict[k] = v
            if not 'parent' in result_dict[k].keys():
                result_dict[k]['parent'] = value

    return result_dict

def rev_eval(tree, cmp_val):
    curr_val = tree['humn']
    prev_val = 'humn'
    operations = []
    while 'parent' in curr_val.keys():
        parent = curr_val['parent']
        curr_val = tree[parent]
        if curr_val['left'] == prev_val:
            operations.append((curr_val['op'], eval(curr_val['right'], tree), parent))
        else:
            operations.append((eval(curr_val['left'], tree), curr_val['op'], parent))
        prev_val = parent

    operations = operations[::-1]
    result = cmp_val

    operand = ''
    prev = result
    val = 0
    for op in operations:
        if type(op[0]) == int:
            if op[1] == '/':
                result = op[0] // result
                operand = '*'
            elif op[1] == '*':
                result = result // op[0]
                operand = '/'
            elif op[1] == '+':
                result = result - op[0]
                operand = '-'
            elif op[1] == '-':
                result = op[0] - result
                operand = '+'
            val = op[0]
        else:
            if op[0] == '/':
                result = op[1] * result
                operand = '*'
            elif op[0] == '*':
                result = result // op[1]# // result
                operand = '/'
            elif op[0] == '+':
                result = result - op[1]
                operand = '-'
            elif op[0] == '-':
                result = op[1] + result
                operand = '+'
            val = op[1]
        prev = result
    return result

def eval(top_item, tree_dict):
    contents = tree_dict[top_item]
    if 'value' in contents.keys():
        return contents['value']
    else:
        left, op, right = contents['left'], contents['op'], contents['right']
        lhs = eval(left, tree_dict)
        rhs = eval(right, tree_dict)
        if op == '+':
            return lhs + rhs
        elif op == '/':
            return lhs // rhs
        elif op == '-':
            return lhs - rhs
        elif op == '*':
            return lhs * rhs

with open('input.txt', 'r') as f:
    lines = [x.split('\n')[0].split(': ') for x in f.readlines()]

value_dict  = {}
for line in lines:
    try:
        value_dict[line[0]] = int(line[1])
    except Exception:
        value_dict[line[0]] = line[1]

lhs, op, rhs = value_dict['root'].split(' ')
left_tree = build_tree(lhs, copy.deepcopy(value_dict))
right_tree = build_tree(rhs, copy.deepcopy(value_dict))

if 'humn' in left_tree.keys():
    rhs_value = eval(rhs, right_tree)
    print(rev_eval(left_tree, rhs_value))

elif 'humn' in right_tree.keys():
    lhs_value = eval(lhs, left_tree)
    print(rev_eval(right_tree, lhs_value))
