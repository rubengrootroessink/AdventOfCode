# Inspired by others
# Apparently using a huge string is good enough for some reason

with open('input.txt') as f:
    nr_recipes = f.read().strip()

queue = '37'

index_1 = 0
index_2 = 1

while not nr_recipes in queue[-7:]:

    recipe_1 = int(queue[index_1])
    recipe_2 = int(queue[index_2])

    queue += str(recipe_1 + recipe_2)

    index_1 = (index_1 + 1 + recipe_1) % len(queue)
    index_2 = (index_2 + 1 + recipe_2) % len(queue)

print(queue.index(nr_recipes))
