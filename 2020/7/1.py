def recursive(dictionary, color):
    curr_color = dictionary[color]
    
    if 'shiny gold' in curr_color.keys():
        return True
    elif curr_color == {}:
        return False
    else:
        return sum([1 for key, value in curr_color.items() if recursive(dictionary, key)]) > 0
    
    return False

big_dict = {}
with open('input.txt', 'r') as file:
    count = 0
    for line in file.readlines():
        data = line.split('\n')[0]
        data = data.split(' bags contain ')
        big_bag = data[0]
        
        if data[1] == 'no other bags.':
            big_dict[big_bag] = {}
        else:
        
            small_bags = data[1].split('.')[0].split(', ')
            small_dict = {}
            for bag in small_bags:
                splitted_bag = bag.split(' ')
                color, amount = splitted_bag[1] + ' ' + splitted_bag[2], int(splitted_bag[0])
                small_dict[color] = amount
            big_dict[big_bag] = small_dict
 
count = 0
for key, value in big_dict.items():
    if recursive(big_dict, key):
        count += 1
print(count)
