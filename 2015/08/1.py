import re

count = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        clean_line = line.split('\n')[0]
        
        data = clean_line
        data = data[1:len(data)-1]
        num_slashes = data.count('\\\\')
        data = data.replace('\\\\', '\\')
        num_quotes = data.count('\\\"')
        data = data.replace('\\\"', '\"')
        
        pattern = re.escape('\\') + 'x[0-9a-f]{2}'
        num_codes = len(re.findall(pattern, data))
        data = re.sub(pattern, '_', data)

        print(clean_line, data, len(clean_line), len(data))
        count += (len(clean_line) - len(data))
        
print(count)
