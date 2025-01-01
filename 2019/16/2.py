# Inspired by others
def transform(input_signal, pattern):
    total = sum(input_signal)
    result = []
    for c in input_signal:
        result.append(((total % 10) + 10) % 10)
        total -= c
    return result

with open('input.txt') as f:
    input_signal = [int(x) for x in f.read().strip()]

pattern = [0, 1, 0, -1]

offset = int("".join([str(x) for x in input_signal[:7]]))
curr_signal = input_signal*10000
curr_signal = curr_signal[offset:]

for i in range(100):
    curr_signal = transform(curr_signal, pattern)

print(''.join([str(x) for x in curr_signal[0:8]]))
