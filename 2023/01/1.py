print(sum([int(''.join(list(map(lambda z: [y for y in x if y.isdigit()][z], [0,-1])))) for x in open('input.txt').read().split('\n')[:-1]]))
