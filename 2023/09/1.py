with open('input.txt') as f:
    data = [list(map(lambda y: int(y), x.split('\n')[0].split())) for x in f.readlines()]

def find_next(seq):
    new_seq = seq
    last_digits = [seq[-1]]
    while not all([new_seq[i] == new_seq[0] for i in range(len(new_seq))]):

        tmp_result = []
        f,l = new_seq[:-1], new_seq[1:]
        for i in range(len(f)):
            tmp_result.append(l[i] - f[i])

        last_digits.append(tmp_result[-1])
        new_seq = tmp_result

    return sum(last_digits)

result = 0
for seq in data:
    result += find_next(seq)

print(result)
