from collections import deque

def split_num(num):
    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)

with open('input.txt') as f:
    nr_recipes = int(f.read())

queue = [3, 7]

index_1 = 0
index_2 = 1

for i in range(nr_recipes+10):

    recipe_1 = queue[index_1]
    recipe_2 = queue[index_2]

    comb = recipe_1 + recipe_2

    queue = queue + split_num(comb)

    index_1 = (index_1 + 1 + recipe_1) % len(queue)
    index_2 = (index_2 + 1 + recipe_2) % len(queue)

print(''.join([str(x) for x in queue[nr_recipes:nr_recipes+10]]))
