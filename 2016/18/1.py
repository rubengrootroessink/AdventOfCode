with open('input.txt') as f:
    start_row = f.read().strip()

num_rows = 40

row_length = len(start_row)
prev_row = start_row

count = prev_row.count('.')

for i in range(num_rows-1):
    new_row = ''
    last_row = '.' + prev_row + '.'
    for i in range(row_length):
        vals = last_row[i:i+3]
        if (vals[0] == '^' and vals[-1] == '.') or (vals[0] == '.' and vals[-1] == '^'):
            new_row += '^'
        else:
            new_row += '.'

    prev_row = new_row
    count += prev_row.count('.')

print(count)
