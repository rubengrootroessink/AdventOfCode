import re

def valid(pass_string):
    data = re.split(' |\n', pass_string)
    print(data)
    fields = {
        'byr': '(19[2-9]\d|200[012])',
        'iyr': '(20(1[0-9]|20))',
        'eyr': '(20(2[0-9]|30))',
        'hgt': '(1([5-8]\d|9[0-3])cm|(59|6[0-9]|7[0-6])in)',
        'hcl': '#[0-9a-fA-F]{6}',
        'ecl': '(amb|blu|brn|gry|grn|hzl|oth)',
        'pid': '[0-9]{9}',
    }
    
    if sum([1 for x in fields.keys() if x in pass_string]) != 7:
        return False
    
    for field in data:
        if field == '':
            break
        field_name, value = field.split(':')
        if field_name != 'cid':
            pattern = re.compile(fields[field_name])
            if pattern.fullmatch(value) is None:
                return False
    return True

count = 0
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    for passport in data:
        if valid(passport):
            count += 1

print(count)
