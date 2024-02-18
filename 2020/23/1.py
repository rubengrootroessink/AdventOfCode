with open('input.txt', 'r') as file:
    cups = [int(x) for x in list(file.read().split('\n')[0])]
    index_current_cup = 0
    for i in range(0, 100):
        clockwise_cups = [cups[(index_current_cup + i) % len(cups)] for i in range(1, 4)]
        
        current_cup = cups[index_current_cup]
        destination_cup = current_cup - 1
        if destination_cup < min(cups):
            destination_cup = max(cups)
        while destination_cup in clockwise_cups:
            destination_cup = destination_cup - 1
            if destination_cup < min(cups):
                destination_cup = max(cups)
                
        index_destination_cup = cups.index(destination_cup)

        new_cups = [x for x in cups if not x in clockwise_cups]
        cups = [destination_cup] + clockwise_cups + [new_cups[(new_cups.index(destination_cup) + i) % len(new_cups)] for i in range(1, len(new_cups))]
        
        index_current_cup = (cups.index(current_cup) + 1) % len(cups)
        
    index_1 = cups.index(1)
    cups = [str(cups[(index_1 + i) % len(cups)]) for i in range(1, len(cups))]

    print("".join(cups))
