from collections import deque

def recursive(q1, q2, level=1):
    count = 0
    c_round = 1
    
    p1_configs = []
    p2_configs = []
    
    while len(q1) != 0 and len(q2) != 0:
        if list(q1) in p1_configs and list(q2) in p2_configs:
            return 'p1', []

        p1_configs.append(list(q1))
        p2_configs.append(list(q2))
        
        p1 = q1.popleft()
        p2 = q2.popleft()
        
        if p1 < len(q1) + 1 and p2 < len(q2) + 1:
            sub_winner, sub_winner_list = recursive(deque(list(q1.copy())[0:p1]), deque(list(q2.copy())[0:p2]), level=level+1)
            if sub_winner == 'p1':
                q1.append(p1)
                q1.append(p2)
            elif sub_winner == 'p2':
                q2.append(p2)
                q2.append(p1)
        elif p1 > p2:
            q1.append(p1)
            q1.append(p2)
        elif p2 > p1:
            q2.append(p2)
            q2.append(p1)
        count += 1
        c_round += 1
        
    winner = 'p1'
    winner_list = q1
    if len(q1) == 0:
        winner = 'p2'
        winner_list = list(q2)
    elif len(q2) == 0:
        winner = 'p1'
        winner_list = list(q1)
        
    return winner, winner_list

with open('input.txt', 'r') as file:
    players = file.read().split('\n\n')
    player_1 = [int(x) for x in players[0].split(':\n')[1].split('\n')]
    player_2 = [int(x) for x in players[1].split(':\n')[1].split('\n') if x != '']

    q1 = deque(player_1)
    q2 = deque(player_2)

    winner, winner_list = recursive(q1, q2)        
    print(sum([x*(len(winner_list)-i) for i, x in enumerate(winner_list)]))
