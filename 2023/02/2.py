import math

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

return_vals = []
for line in data:
    color_dict = {key: 0 for key in ['red', 'green', 'blue']}
    game_id, game_values = line.split(': ')
    game_id = int(game_id.split(' ')[1])
    hands = game_values.split('; ')
    
    possible = True
    for hand in hands:
        hand_vals = hand.split(', ')
        for item in hand_vals:
            nr, color = [int(x) if i == 0 else x for i, x in enumerate(item.split(' '))]
            if nr > color_dict[color]:
                color_dict[color] = nr

    return_vals.append(math.prod(color_dict.values()))

print(sum(return_vals))
