with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [list(map(int, x.split('\n')[0].split())) for x in lines]  
    
    new_lines = [(x[0] + x[1] > x[2], x[0] + x[2] > x[1], x[1] + x[2] > x[0]) for x in lines]
    new_lines = [True for x in new_lines if x[0] and x[1] and x[2]]
    print(len(new_lines))
