def generator(start, factor, mod_val, cmp_val):
    result = start
    while True:
        result = (result * factor) % mod_val
        if result % cmp_val == 0:
            yield result

with open('input.txt') as f:
    a_start, b_start = [int(x.strip().split('with ')[1]) for x in f.readlines()]

a_factor = 16807
b_factor = 48271

mod_val = 2147483647

a = generator(a_start, a_factor, mod_val, 4)
b = generator(b_start, b_factor, mod_val, 8)

count = 0
for i in range(5000000):
    a_curr, b_curr = next(a), next(b)

    if a_curr & 0xFFFF == b_curr & 0xFFFF:
        count += 1

print(count)
