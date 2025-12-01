import re, math
d, c, p = 50, 0, 1
[(d := d + o, c := c + math.floor(abs(d) // 100) + (d < 0) + (d == 0) - (p == 0 and o < 0), d := d % 100, p := d) for o in [int(x) for x in re.findall(r'-?\d+', open('input.txt').read().replace('L', '-'))]]
print(c)
