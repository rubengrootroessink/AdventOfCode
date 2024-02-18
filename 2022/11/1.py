import re
import math
import copy

def round(monkey_list):
    result_list = monkey_list
    for monkey in result_list:
        for item in monkey['items_holding']:
            worry_level = item
            
            f_hand, op, s_hand = monkey['operation'].split(' ')
            
            f_hand = worry_level
            s_hand = worry_level if s_hand == 'old' else int(s_hand)

            if op == '*':
                worry_level = f_hand * s_hand
            elif op == '+':
                worry_level = f_hand + s_hand
            elif op == '-':
                worry_levle = f_hand - s_hand
            else:
                assert False

            worry_level = math.floor(worry_level / 3)
            
            if worry_level % monkey['test'] == 0:
                result_list[monkey['if_true']]['items_holding'].append(worry_level)
            else:
                result_list[monkey['if_false']]['items_holding'].append(worry_level)
            
            result_list[monkey['monkey_id']]['nr_inspections'] += 1
        result_list[monkey['monkey_id']]['items_holding'] = []

    return result_list

def parse_monkey(monkey_string):
    pattern = r'^Monkey (\d+):\n  Starting items: ([0-9 ,]+)\n  Operation: new = (old [\+\*\/\-] [a-z0-9]+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)'
    matcher = re.search(pattern, monkey_string)
    
    result_dict = {}
    result_dict['monkey_id'] = int(matcher.group(1))
    result_dict['items_holding'] = [int(x) for x in matcher.group(2).split(', ')]
    result_dict['operation'] = matcher.group(3)
    result_dict['test'] = int(matcher.group(4))
    result_dict['if_true'] = int(matcher.group(5))
    result_dict['if_false'] = int(matcher.group(6))
    result_dict['nr_inspections'] = 0

    return result_dict

with open('input.txt', 'r') as f:
    monkeys = f.read()[:-1].split('\n\n')
    monkeys = [parse_monkey(x) for x in monkeys]

for i in range(0, 20):
    result_dict = round(monkeys)

result = math.prod(sorted([monkey['nr_inspections'] for monkey in result_dict])[-2:])
print(result)
