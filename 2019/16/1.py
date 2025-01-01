def transform(input_signal, pattern):
    result = []
    for d in range(len(input_signal)):
        res = 0
        for i, c in enumerate(input_signal):
            if i < d:
                continue
            res += c*pattern[((i+1)//(d+1))%4]
        result.append(abs(res)%10)
    return result

with open('input.txt') as f:
    input_signal = [int(x) for x in f.read().strip()]

pattern = [0, 1, 0, -1]
curr_signal = input_signal

for i in range(100):
    curr_signal = transform(curr_signal, pattern)

print(''.join([str(x) for x in curr_signal[0:8]]))
