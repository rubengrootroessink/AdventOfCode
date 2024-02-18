from itertools import product

pos_1, pos_2 = 0, 0
with open('input.txt') as f:
    pos_1, pos_2 = [int(x.split('position: ')[1]) for x in f.readlines()]

cart_prod = list(product([1,2,3], repeat=3))
count_dict = {}
for item in cart_prod:
    total = sum(item)
    if total in count_dict.keys():
        count_dict[total] += 1
    else:
        count_dict[total] = 1

def step(moves, pos, score):
    new_pos = (pos + moves) % 10
    new_pos = new_pos if new_pos != 0 else 10
    new_score = score + new_pos
    return new_pos, new_score

def turn(universes, turn_1):
    new_universes = []
    blackjack = 0
    for universe in universes:
        for moves, num in count_dict.items():
            if turn_1:
                pos, score = universe['pos_1'], universe['score_1']
            else:
                pos, score = universe['pos_2'], universe['score_2']

            new_pos, new_score = step(moves, pos, score)
            if new_score >= 21:
                blackjack += num * universe['num_occurrences']
            elif turn_1:
                new_universe = {
                    'pos_1': new_pos,
                    'score_1': new_score,
                    'pos_2': universe['pos_2'],
                    'score_2': universe['score_2'],
                    'num_occurrences': num * universe['num_occurrences']

                }
                new_universes.append(new_universe)
            else:
                new_universe = {
                    'pos_1': universe['pos_1'],
                    'score_1': universe['score_1'],
                    'pos_2': new_pos,
                    'score_2': new_score,
                    'num_occurrences': num * universe['num_occurrences']
                }
                new_universes.append(new_universe)
    return new_universes, blackjack

score_1, score_2 = 0, 0
turn_1 = True

universes = [
    {
        'pos_1': pos_1,
        'pos_2': pos_2,
        'score_1': score_1,
        'score_2': score_2,
        'num_occurrences': 1,
    }
]

player_1_wins, player_2_wins = 0, 0
while len(universes) != 0:
    universes, blackjack = turn(universes, turn_1)
    if turn_1:
        player_1_wins += blackjack
    else:
        player_2_wins += blackjack
    turn_1 = not turn_1

print(player_1_wins if player_1_wins > player_2_wins else player_2_wins)
