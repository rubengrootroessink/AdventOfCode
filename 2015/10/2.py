import re

def look_and_say(string):
    result = ""
    
    indices = [0]
    for i in range(0, len(data)):
        if data[i] != data[indices[-1]]:
            indices.append(i)
    
    extra_indices = indices + [len(string)]
    lengths = [extra_indices[i+1]-extra_indices[i] for i in range(len(extra_indices)-1)]
    
    for i, index in enumerate(indices):
        result += str(lengths[i]) + string[index]
    return result

with open('input.txt', 'r') as file:
    data = file.read().split('\n')[0]
    for i in range(0, 50):
        data = look_and_say(data)
    print(len(data))
