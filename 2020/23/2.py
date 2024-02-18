cups = {}
start_cup = 0

def print_string(cups, start_cup):
    result = str(start_cup)
    current_cup = cups[start_cup]
    while current_cup != start_cup:
        result += str(current_cup)
        current_cup = cups[current_cup]
    return result
    
num_cups = 1000000
with open('input.txt', 'r') as file:
    listed_cups = [int(x) for x in list(file.read().split('\n')[0])]
    start_cup = listed_cups[0]
    last = max(listed_cups)
    for i in range(0, len(listed_cups)-1):
        cups[listed_cups[i]] = listed_cups[i+1]
        
    prev = listed_cups[-1]
    for num in range(last + 1, num_cups + 1):
        cups[prev] = num
        prev = num
    cups[prev] = listed_cups[0]

current_cup = start_cup
nr_runs = 10000000
for i in range(0, nr_runs):
    one_cup_down = cups[current_cup]
    two_cups_down = cups[one_cup_down]
    three_cups_down = cups[two_cups_down]
    
    clockwise_cups = [one_cup_down, two_cups_down, three_cups_down]

    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = num_cups
    while destination_cup in clockwise_cups:
        destination_cup = destination_cup - 1
        if destination_cup == 0:
            destination_cup = num_cups

    four_cups_down = cups[three_cups_down]
    destination_next = cups[destination_cup]

    cups[current_cup] = four_cups_down
    cups[destination_cup] = one_cup_down
    cups[three_cups_down] = destination_next
    current_cup = cups[current_cup]

first = cups[1]
second = cups[first]
print(first * second)
