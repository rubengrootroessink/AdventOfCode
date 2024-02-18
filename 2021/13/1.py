dots = []
folds = []
with open('input.txt') as file:
    dots, folds = file.read().split('\n\n')
    dots = [(int(y) for y in x.split(',')) for x in dots.split('\n')]
    folds = [x.split('fold along ')[1].split('=') for x in folds.split('\n') if x != '']

fold_direction, fold_val = folds[0]
fold_val = int(fold_val)
if fold_direction == 'x':
    dots = list(set([(2 * fold_val - x, y) if x > fold_val else (x, y) for x, y in dots]))
elif fold_direction == 'y':
    dots = list(set([(x, 2 * fold_val - y) if y > fold_val else (x, y) for x, y in dots]))

print(len(dots))
