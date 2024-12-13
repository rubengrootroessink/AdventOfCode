with open('input.txt') as f:
    blocks = f.read().strip().split('\n\n')

count = 0
for block in blocks:

    a, b, p = block.split('\n')
    ax = float(a.split('A: X+')[1].split(',')[0])
    ay = float(a.split('Y+')[1])
    bx = float(b.split('B: X+')[1].split(',')[0])
    by = float(b.split('Y+')[1])
    px = float(p.split('X=')[1].split(',')[0])
    py = float(p.split('Y=')[1])

    n = int((bx * py - by * px ) / (bx * ay - by * ax))
    m = int((px - ax * n) / bx)

    eq_1 = ax * n + bx * m == px
    eq_2 = ay * n + by * m == py

    if eq_1 and eq_2:
        count +=  n*3 + m

print(count)
