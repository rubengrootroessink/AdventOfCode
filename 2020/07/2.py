def recursive(dictionary, color):
    curr_color = dictionary[color]

    count = 0
    if len(curr_color) == 0:
        count = 1
        return count
    else:
        for key, value in curr_color.items():
            count += recursive(dictionary, key) * value
        count += 1
    return count

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
 
print(recursive(big_dict, 'shiny gold') - 1)
