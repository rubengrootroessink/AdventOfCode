import re

count = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        clean_line = line.split('\n')[0]
        
        data = clean_line
        data = data.replace('\\', '\\\\')
        data = data.replace('"', '\\"')
        data = '"' + data + '"'
        count += (len(data) - len(clean_line))
        
print(count)
