import re
from functools import reduce

def chinese_remainder(remainders, modulos):
    summation = 0
    product = reduce(lambda acc, b: acc*b, modulos)
    for r_i, m_i in zip(remainders, modulos):
        p = product // m_i
        summation += r_i * mul_inv(p, m_i) * p
    return summation % product

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('input.txt') as f:
    discs = [x.strip() for x in f.readlines()]

remainders = []
modulos = []

pattern = r'Disc #(\d+) has (\d+) positions?; at time=0, it is at position (\d+)\.' 
for disc in discs:
    groups = re.match(pattern, disc).groups()
    disc_num, num_pos, s_pos = [int(x) for x in groups]

    # (s_pos + disc_num + start_press) % mod_disc == 0
    # => start_press % mod_disc == -(s_pos + disc_num) % mod_disc

    remainders.append(-(s_pos + disc_num) % num_pos)
    modulos.append(num_pos)

# Additional disk
remainders.append(-(0 + len(discs) + 1) % 11)
modulos.append(11)

print(chinese_remainder(remainders, modulos))
