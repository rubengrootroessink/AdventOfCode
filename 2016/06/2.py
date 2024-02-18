from collections import Counter

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [list(line.split('\n')[0]) for line in lines]
    
    result = ''
    for col_nr in range(len(lines[0])):
        temp_str = ''
        for row_nr in range(len(lines)):
            temp_str += lines[row_nr][col_nr]
        result += sorted(dict(Counter(temp_str)).items(), key=lambda x: x[1])[0][0]
    print(result)
