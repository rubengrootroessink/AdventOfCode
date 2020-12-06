count = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0].split(' ')
        first, second = int(data[0].split('-')[0]), int(data[0].split('-')[1])
        letter = data[1].split(':')[0]
        passwd = data[2]
        
        value = (passwd[first - 1] == letter) != (passwd[second - 1] == letter)
        if value:
            count += 1
            
print(count)
