def fold(fold_direction, fold_val, dots):
    if fold_direction == 'x':
        dots = list(set([(2 * fold_val - x, y) if x > fold_val else (x, y) for x, y in dots]))
    elif fold_direction == 'y':
        dots = list(set([(x, 2 * fold_val - y) if y > fold_val else (x, y) for x, y in dots]))
    return dots

folds = []
with open('input.txt') as file:
    dots, folds = file.read().split('\n\n')
    dots = [(int(y) for y in x.split(',')) for x in dots.split('\n')]
    folds = [x.split('fold along ')[1].split('=') for x in folds.split('\n') if x != '']

for fold_direction, fold_val in folds:
    int_val = int(fold_val)
    dots = fold(fold_direction, int_val, dots)

max_x = max([x[0] for x in dots])
max_y = max([x[1] for x in dots])

for y in range(0, max_y + 1):
    row = []
    for x in range(0, max_x + 1):
        if (x, y) in dots:
            row.append('#')
        else:
            row.append(' ')
    print(''.join(row))
