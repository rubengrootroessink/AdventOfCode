print(sum(map(lambda z: max(z)-min(z), [[int(y) for y in x.split('\n')[0].split()] for x in open('input.txt').readlines()])))
