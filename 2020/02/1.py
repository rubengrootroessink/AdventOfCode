count = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0].split(' ')
        at_least, at_most = int(data[0].split('-')[0]), int(data[0].split('-')[1])
        letter = data[1].split(':')[0]
        passwd = data[2]
        
        letter_count = sum([1 for x in passwd if x == letter])
        if letter_count <= at_most and letter_count >= at_least:
            count += 1
            
print(count)
