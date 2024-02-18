def corrupted_line(line):
    match_dict = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>'
    }
    open_chars = [line[0]]
    if line[0] in ['}', ')', ']', '>']:
        return True, []
    for elem in line[1:]:
        if elem in ['}', ')', ']', '>']:
            if match_dict[open_chars[-1]] == elem:
                open_chars.pop()
            else:
                return True, []
        else:
            open_chars.append(elem)
    closing_chars = list(reversed([match_dict[x] for x in open_chars]))
    return False, closing_chars

input_matrix = []
with open('input.txt') as file:
    input_matrix = [x.split('\n')[0] for x in file.readlines()]
value_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
scores = []
for line in input_matrix:
    corrupted, chars = corrupted_line(line)
    if not corrupted:
        score = 0
        [(score := (score * 5) + value_dict[x]) for x in chars]
        scores.append(score)
print(list(sorted(scores))[(len(scores) - 1)//2])
