import re

count = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        clean_line = line.split('\n')[0]
        
        data = clean_line
        data = data[1:len(data)-1]
        data = data.replace('\\\\', '_')
        data = data.replace('\\\"', '_')
        pattern = re.escape('\\') + 'x[0-9a-f]{2}'
        data = re.sub(pattern, '_', data)
        count += (len(clean_line) - len(data))
        
print(count)

