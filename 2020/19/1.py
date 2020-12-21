import re

def evaluate(rule_dict, curr_val):
    evaluated_val = rule_dict[curr_val]
    
    rule_options = evaluated_val.split(' | ')
    
    return_string = False
    
    return_val = []
    for option in rule_options:
        rules = option.split(' ')
        option_string = ""
        for rule in rules:
            if rule.isnumeric():
                option_string += evaluate(rule_dict, int(rule))
            else:
                return_string = True
                option_string += rule

        return_val.append(option_string)

    if return_string or curr_val == 0:
        return "|".join(return_val)
    else:
        return "(" + "|".join(return_val) + ")"
        

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    rules = data[0]
    inputs = data[1]

    rule_dict = {}
    for rule in rules.split('\n'):
        rule_data = rule.split(': ')
        if '|' in rule_data[1] and not '"' in rule_data[1]:
            rule_dict[int(rule_data[0])] = rule_data[1]
        else:
            rule_dict[int(rule_data[0])] = rule_data[1].replace('"', '')

    matching_regex = evaluate(rule_dict, 0)

    regex = re.compile(r"" + matching_regex)
    count = 0
    for input_str in inputs.split('\n'):
        if re.fullmatch(regex, input_str):
            count += 1
    print(count)
