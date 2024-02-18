from_snafu_dict = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def from_snafu(number):
    rev = number[::-1]
    result = 0
    for i, digit in enumerate(rev):
        result += from_snafu_dict[digit] * 5**i
    return result

def to_snafu(number):
    if number == 0:
        return ''

    tmp_val = number % 5
    if tmp_val in [0, 1, 2]:
        return to_snafu(number // 5) + str(tmp_val)
    elif tmp_val == 3:
        return to_snafu(1 + number // 5) + '='
    elif tmp_val == 4:
        return to_snafu(1 + number // 5) + '-'

with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

total = 0
for x in data:
    total += from_snafu(x)

print(to_snafu(total))
