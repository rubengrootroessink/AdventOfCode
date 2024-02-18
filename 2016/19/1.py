with open('input.txt') as f:
    num_elves = int(f.read())

curr_vals = list(range(num_elves+1))

while len(curr_vals) > 1:
    new_vals = []
    for i in range(0, len(curr_vals)):
        if i % 2 == 0:
            new_vals.append(curr_vals[i])

    if len(curr_vals) % 2 != 0:
        new_vals = new_vals[1:]

    curr_vals = new_vals

print(curr_vals[0])
