# Bruteforce solution, can be improved using CRT (I did not look too much into it)
with open('input.txt') as f:
    layer_dict = {x: ((y - 2) * 2 + 2) for (x, y) in [tuple(map(int, x.strip().split(': '))) for x in f.readlines()]}

T = 0
found = False
while not found:

    wrong = False
    for depth in layer_dict.keys():
        period_length = layer_dict[depth]

        if (depth + T) % period_length == 0:
            wrong = True
            break

    if not wrong:
        found = True
    else:
        T += 1

print(T)
