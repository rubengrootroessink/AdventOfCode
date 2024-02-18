from collections import Counter

card_space = list('AKQT98765432J') # Changed joker position

with open('input.txt') as f:
    data = [x.split()[0:2] for x in f.readlines()]

sortable_hands = []
for tmp_val in data:
    hand = tmp_val
    sorted_hand = [card_space.index(x) for x in hand[0]]
    splitted = Counter(hand[0])
    mc = splitted.most_common()
    
    hand_type = [x[1] for x in mc]
    
    if 'J' in hand[0]:
        if hand_type == [5]:
            hand[0] = hand[0].replace('J', 'A')
        elif hand_type == [4,1] or hand_type == [3,2]:
            if mc[0][0] == 'J':
                hand[0] = hand[0].replace('J', mc[1][0])
            else:
                hand[0] = hand[0].replace('J', mc[0][0])
        elif hand_type == [3,1,1]:
            if mc[0][0] == 'J':
                hand[0] = hand[0].replace('J', card_space[min([card_space.index(x) for x in [mc[1][0], mc[2][0]]])])
            else:
                hand[0] = hand[0].replace('J', mc[0][0])
        elif hand_type == [2,2,1]:
            if mc[0][0] == 'J':
                hand[0] = hand[0].replace('J', mc[1][0])
            elif mc[1][0] == 'J':
                hand[0] = hand[0].replace('J', mc[0][0])
            else:
                hand[0] = hand[0].replace('J', card_space[min([card_space.index(x) for x in [mc[0][0], mc[1][0]]])])
        elif hand_type == [2,1,1,1]:
            if mc[0][0] == 'J':
                hand[0] = hand[0].replace('J', card_space[min([card_space.index(x) for x in [mc[0][0], mc[1][0], mc[2][0], mc[3][0]]])])
            else:
                hand[0] = hand[0].replace('J', mc[0][0])
        elif hand_type == [1,1,1,1,1]:
            hand[0] = hand[0].replace('J', card_space[min([card_space.index(x[0]) for x in mc])])

        splitted = Counter(hand[0])
        mc = splitted.most_common()

    if len(splitted) == 1:
        sortable_hands.append((hand[0], int(hand[1]), [0] + sorted_hand)) # Five of a kind
    elif len(splitted) == 2:
        if mc[0][1] == 4:
            sortable_hands.append((hand[0], int(hand[1]), [1] + sorted_hand)) # Four of a kind
        else:
            sortable_hands.append((hand[0], int(hand[1]), [2] + sorted_hand)) # Full house
    elif len(splitted) == 3:
        if mc[0][1] == 3:
            sortable_hands.append((hand[0], int(hand[1]), [3] + sorted_hand)) # Three of a kind
        else:
            sortable_hands.append((hand[0], int(hand[1]), [4] + sorted_hand)) # Two pair
    elif len(splitted) == 4:
        sortable_hands.append((hand[0], int(hand[1]), [5] + sorted_hand)) # One pair
    else:
        sortable_hands.append((hand[0], int(hand[1]), [6] + sorted_hand)) # High Card

sorted_hands = sorted(sortable_hands, key=lambda x: x[2])
print(sum([x[1]*(len(sorted_hands)-i) for i, x in enumerate(sorted_hands)]))
