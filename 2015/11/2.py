import re

def increase(nr_list):
    nr_list[-1] = nr_list[-1] + 1
    while 123 in nr_list:
        index = nr_list.index(123)
        nr_list[index] = 97
        nr_list[index-1] = nr_list[index-1] + 1
    return nr_list
    
def check(nr_list):
    if 105 in nr_list or 111 in nr_list or 108 in nr_list: # i, o or l in the password
        return False
    else:
        match_doubles = re.match(r'[a-z]*([a-z])\1[a-z]*([a-z])\2[a-z]*', "".join([chr(x) for x in nr_list]))
        if not match_doubles:
            return False
        else:
            diff_list = [j-i for i, j in zip(nr_list[:-1], nr_list[1:])]
            match_subsequent_row = re.match(r'.*(a)\1.*', "".join([chr(x + 96) for x in diff_list]))
            if match_subsequent_row:
                return True
            else:
                return False

with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0]
    data_list = list(data)
    nr_list = [ord(x) for x in data_list]
    
    found = check(nr_list)
    count = 0
    while not found:
        nr_list = increase(nr_list)
        count += 1
        password = "".join([chr(x) for x in nr_list])
        if password != 'hxbxxyzz':
            found = check(nr_list)
    print("".join([chr(x) for x in nr_list]))
