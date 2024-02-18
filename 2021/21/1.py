pos_1, pos_2 = 0, 0
with open('input.txt') as f:
    pos_1, pos_2 = [int(x.split('position: ')[1]) for x in f.readlines()]

def step(die_val, pos, score):
    moves = []
    for i in range(0, 3):
        moves.append(die_val)
        die_val = (die_val % 100) + 1
    new_pos = (pos + sum(moves)) % 10
    new_pos = new_pos if new_pos != 0 else 10
    new_score = score + new_pos
    return die_val, new_pos, new_score

die_val = 1
die_runs = 0
score_1, score_2 = 0, 0
turn_1 = True
while score_1 < 1000 and score_2 < 1000:
    if turn_1:
        die_val, pos_1, score_1 = step(die_val, pos_1, score_1)
    elif not turn_1: 
        die_val, pos_2, score_2 = step(die_val, pos_2, score_2)
    turn_1 = not turn_1
    die_runs += 3

print(min(score_1, score_2) * die_runs)
