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
                if int(rule) == 42 and curr_val == 8:
                    option_string += '+'
                if curr_val == 11:
                    option_string = ''
                    return_string = True
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
    
    regex_31 = evaluate(rule_dict, 31)
    regex_42 = evaluate(rule_dict, 42)
    
    regexes = []
    for i in range(1, 50):
        new_regex = matching_regex + i*regex_42 + i*regex_31
        regexes.append(new_regex)
    
    result_count = 0
    for input_str in inputs.split('\n'):
        count = 0
        for rex in regexes:
            regex = re.compile(r"" + rex)
            if re.fullmatch(regex, input_str):
                regex = re.compile(r"" + new_regex)
                count += 1
        if count > 0:
            result_count += 1
            
    print(result_count)
