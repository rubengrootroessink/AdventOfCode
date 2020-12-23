from collections import deque

with open('input.txt', 'r') as file:
    players = file.read().split('\n\n')
    player_1 = [int(x) for x in players[0].split(':\n')[1].split('\n')]
    player_2 = [int(x) for x in players[1].split(':\n')[1].split('\n') if x != '']

    q1 = deque(player_1)
    q2 = deque(player_2)
    while len(q1) != 0 and len(q2) != 0:
        p1 = q1.popleft()
        p2 = q2.popleft()
        if p1 > p2:
            q1.append(p1)
            q1.append(p2)
        elif p2 > p1:
            q2.append(p2)
            q2.append(p1)
        
    winner = list(q1)
    if len(q1) == 0:
        winner = list(q2)
    elif len(q2) == 0:
        winner = list(q1)
        
    print(sum([x*(len(winner)-i) for i, x in enumerate(winner)]))
