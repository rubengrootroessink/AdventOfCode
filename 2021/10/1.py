def check_line(line):
    match_dict = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>'
    }
    open_chars = [line[0]]
    if line[0] in ['}', ')', ']', '>']:
        return line[0]
    for elem in line[1:]:
        if elem in ['}', ')', ']', '>']:
            if match_dict[open_chars[-1]] == elem:
                open_chars.pop()
            else:
                return elem
        else:
            open_chars.append(elem)
    return None

input_matrix = []
with open('input.txt') as file:
    input_matrix = [x.split('\n')[0] for x in file.readlines()]

value_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
result = []
for line in input_matrix:
    result.append(check_line(line)) 
print(sum([value_dict[x] for x in result if not x is None]))
