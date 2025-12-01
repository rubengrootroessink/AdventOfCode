import re
d, c = 50, 0
[(d := (d + o) % 100, c := c + (d == 0)) for o in [int(x) for x in re.findall(r'-?\d+', open('input.txt').read().replace('L', '-'))]]
print(c)
