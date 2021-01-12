import itertools
from functools import reduce

def combinations(nr, nr_buckets):
    combination_dict = []
    check = [sub_item for sub_item in range(1, nr)]

    for i in itertools.product(check, repeat=nr_buckets):
        if sum(i) == nr:
            combination_dict.append(i)

    return combination_dict

def calc_chars(ingredients, division, chars, ingredient_dict):
    ings_dict = {}
    
    calories = 0
    for i, ing in enumerate(ingredients):
        calories += ingredient_dict[ing]['calories'] * division[i]
        ings_dict[ing] = division[i]
        
    if calories != 500:
        return 0
        
    score_list = []
    for char in chars:
        sub_score = 0
        for ingredient in ingredients:
            sub_score += ingredient_dict[ingredient][char] * ings_dict[ingredient]
        sub_score = 0 if sub_score < 0 else sub_score
        score_list.append(sub_score)
    return reduce((lambda x, y: x * y), score_list)

with open('input.txt', 'r') as f:
    ingredient_dict = {}
    for data in f.readlines():
        line = data.split('\n')[0].split(': ')
        ingredient = line[0]
        vals = line[1].split(', ')
        value_dict = {}
        for val in vals:
            key, value = val.split(' ')
            value = int(value)
            value_dict[key] = value
        ingredient_dict[ingredient] = value_dict

    chars = [x for x in ingredient_dict[list(ingredient_dict.keys())[0]] if x != 'calories']
    ingredients = list(sorted(ingredient_dict.keys()))
    
    combs = combinations(100, len(ingredients))
    top_score = 0
    for comb in combs:
        result = calc_chars(ingredients, comb, chars, ingredient_dict)          
        if result > top_score:
            top_score = result
    print(top_score)
