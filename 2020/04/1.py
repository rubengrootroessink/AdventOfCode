def valid(pass_string):
    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for field in fields:
        if not field in pass_string:
            return False
    return True

count = 0
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    for passport in data:
        if valid(passport):
            count += 1

print(count)    
