with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

color_dict = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

non_matching_games = []
for line in data:
    game_id, game_values = line.split(': ')
    game_id = int(game_id.split(' ')[1])
    hands = game_values.split('; ')
    
    possible = True
    for hand in hands:
        hand_vals = hand.split(', ')
        for item in hand_vals:
            nr, color = item.split(' ')
            if int(nr) > color_dict[color]:
                possible = False

    if possible:
        non_matching_games.append(game_id)

print(sum(non_matching_games))
