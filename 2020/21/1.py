with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    data_dict = {}
    allergens_list = []
    ingredients_list = []
    
    for i, line in enumerate(lines):
        data = line.split(')\n')[0].split(' (contains ')
        ingredients = data[0].split(' ')
        allergens = data[1].split(', ')
        
        data_dict[i] = {'ingredients': ingredients, 'allergens': allergens}
        
        for allergen in allergens:
            allergens_list.append(allergen)
            
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
    
    mapped_dict = {}
    allergens_list = list(set(allergens_list))
    
    while len(mapped_dict) != len(allergens_list):
        for allergen in allergens_list:
            result_list = []
            for key, value in data_dict.items():
                if allergen in value['allergens']:
                    result_list.append(value['ingredients'])
        
            result = list(set.intersection(*map(set, result_list)) - set(mapped_dict.values()))
            if len(result) == 1:
                mapped_dict[allergen] = result[0]
                
    count = 0
    for ingredient in list(set(ingredients_list) - set(mapped_dict.values())):
        for key, value in data_dict.items():
            if ingredient in value['ingredients']:
                count += 1
                
    print(count)
