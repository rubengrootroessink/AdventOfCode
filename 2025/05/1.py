with open('input.txt') as f:
    ranges, ingredients = f.read().split('\n\n')
    ranges = [range(int(x.split('-')[0]), int(x.split('-')[1])+1) for x in ranges.strip().split('\n')]
    ingredients = [int(x) for x in ingredients.strip().split('\n')]

count = 0
for ing in ingredients:
    if any(ing in r for r in ranges):
        count += 1

print(count)
