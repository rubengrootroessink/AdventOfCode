import re

with open('input.txt') as f:
    board = [x.split('\n')[0] for x in f.readlines()]

p = re.compile('\d+')

non_symbols = [str(x) for x in range(0, 10)] + ['.']

parts = []

for i, row in enumerate(board):
    for match in p.finditer(row):
        part_id = int(match.group())
        start_index, end_index = match.span()

        surrounding_vals = ''
        
        if not start_index <= 0:
            surrounding_vals += row[start_index-1]
        if not end_index == len(row):
            surrounding_vals += row[end_index]

        start_index = 0 if start_index == 0 else start_index - 1
        end_index = len(row)-1 if end_index == len(row)-1 else end_index+1

        if i == 0:
            surrounding_vals += board[i+1][start_index:end_index]
        elif i == len(board)-1:
            surrounding_vals += board[i-1][start_index:end_index]
        else:
            surrounding_vals += board[i+1][start_index:end_index]
            surrounding_vals += board[i-1][start_index:end_index]
        
        if not all([x in non_symbols for x in surrounding_vals]):
            parts.append(part_id)

print(sum(parts))
