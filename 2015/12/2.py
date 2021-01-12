import json

def list_check(listed):
    result = 0
    for elem in listed:
        if type(elem) == int:
            result += elem
        elif type(elem) == dict:
            result += dict_check(elem)
        elif type(elem) == list:
            result += list_check(elem)
    return result

def dict_check(dictionary):
    if 'red' in dictionary.values():
        return 0
    else:
        result = 0
        for key, value in dictionary.items():
            if type(value) == int:
                result += value
            elif type(value) == list:
                result += list_check(value)
            elif type(value) == dict:
                result += dict_check(value)
        return result

with open('input.txt', 'r') as f:
    data = json.load(f)
    
    if type(data) == dict:
        value = dict_check(data)
        print(value)
