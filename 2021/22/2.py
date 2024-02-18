import re

def overlap_once(old, new):
    if new[0] > old[1] or old[0] > new[1]:
        return False
    if old[0] >= new[0] and old[1] <= new[1]:
        return []
    elif old[0] <= new[0] and old[1] <= new[1]:
        return [[old[0], new[0]-1]]
    elif old[0] >= new[0] and old[1] >= new[1]:
        return [[new[1]+1, old[1]]]
    else:
        return [[old[0], new[0]-1], [new[1]+1, old[1]]]

def calc_remove(rem_val, old):
    if old[0] <= rem_val[0] and old[1] >= rem_val[1]: 
        return rem_val
    elif old[0] >= rem_val[0] and old[1] >= rem_val[1]:
        return [old[0], rem_val[1]]
    elif old[0] <= rem_val[0] and old[1] <= rem_val[1]:
        return [rem_val[0], old[1]]
    else:
        return [old[0], old[1]]

def split(prev, rem):
    x_old, y_old, z_old = prev
    x_rem, y_rem, z_rem = rem
    x_new = overlap_once(x_old, x_rem)
    y_new = overlap_once(y_old, y_rem)
    z_new = overlap_once(z_old, z_rem)

    if x_new == False or y_new == False or z_new == False:
        return [(x_old, y_old, z_old)]

    x_rem = calc_remove(x_rem, x_old)
    y_rem = calc_remove(y_rem, y_old)
    z_rem = calc_remove(z_rem, z_old)

    new_values = []
    if x_new == [] and y_new == [] and z_new == []:
        return []
    elif y_new == [] and z_new == []:
        if len(x_new) == 1:
            new_values.append((x_new[0], y_old, z_old))
        else:
            x_fst, x_snd = x_new
            new_values.append((x_fst, y_old, z_old))
            new_values.append((x_snd, y_old, z_old))
    elif x_new == [] and z_new == []:
        if len(y_new) == 1:
            new_values.append((x_old, y_new[0], z_old))
        else:
            y_fst, y_snd = y_new
            new_values.append((x_old, y_fst, z_old))
            new_values.append((x_old, y_snd, z_old))
    elif x_new == [] and y_new == []:
        if len(z_new) == 1:
            new_values.append((x_old, y_old, z_new[0]))
        else:
            z_fst, z_snd = z_new
            new_values.append((x_old, y_old, z_fst))
            new_values.append((x_old, y_old, z_snd))
    elif z_new == []:
        if len(x_new) == 1 and len(y_new) == 1:
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_new[0], z_old))
        elif len(x_new) == 1:
            y_fst, y_snd = y_new
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_fst, z_old))
            new_values.append((x_rem, y_snd, z_old))
        elif len(y_new) == 1:
            x_fst, x_snd = x_new
            new_values.append((x_old, y_new[0], z_old))
            new_values.append((x_fst, y_rem, z_old))
            new_values.append((x_snd, y_rem, z_old))
        else:
            x_fst, x_snd = x_new
            y_fst, y_snd = y_new
            new_values.append((x_fst, y_old, z_old))
            new_values.append((x_snd, y_old, z_old))
            new_values.append((x_rem, y_fst, z_old))
            new_values.append((x_rem, y_snd, z_old))
    elif y_new == []:
        if len(x_new) == 1 and len(z_new) == 1:
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_old, z_new[0]))
        elif len(x_new) == 1:
            z_fst, z_snd = z_new
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_old, z_fst))
            new_values.append((x_rem, y_old, z_snd))
        elif len(z_new) == 1:
            x_fst, x_snd = x_new
            new_values.append((x_old, y_old, z_new[0]))
            new_values.append((x_fst, y_old, z_rem))
            new_values.append((x_snd, y_old, z_rem))
        else:
            x_fst, x_snd = x_new
            z_fst, z_snd = z_new
            new_values.append((x_fst, y_old, z_old))
            new_values.append((x_snd, y_old, z_old))
            new_values.append((x_rem, y_old, z_fst))
            new_values.append((x_rem, y_old, z_snd))
    elif x_new == []:
        if len(y_new) == 1 and len(z_new) == 1:
            new_values.append((x_old, y_old, z_new[0]))
            new_values.append((x_old, y_new[0], z_rem))
        elif len(y_new) == 1:
            z_fst, z_snd = z_new
            new_values.append((x_old, y_new[0], z_old))
            new_values.append((x_old, y_rem, z_fst))
            new_values.append((x_old, y_rem, z_snd))
        elif len(z_new) == 1:
            y_fst, y_snd = y_new
            new_values.append((x_old, y_old, z_new[0]))
            new_values.append((x_old, y_fst, z_rem))
            new_values.append((x_old, y_snd, z_rem))
        else:
            y_fst, y_snd = y_new
            z_fst, z_snd = z_new
            new_values.append((x_old, y_old, z_fst))
            new_values.append((x_old, y_old, z_snd))
            new_values.append((x_old, y_fst, z_rem))
            new_values.append((x_old, y_snd, z_rem))
    else:        
        if len(x_new) == 1 and len(y_new) == 1 and len(z_new) == 1:
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_old, z_new[0]))
            new_values.append((x_rem, y_new[0], z_rem))
        elif len(x_new) == 1 and len(y_new) == 1:
            z_fst, z_snd = z_new
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_new[0], z_old))
            new_values.append((x_rem, y_rem, z_fst))
            new_values.append((x_rem, y_rem, z_snd))
        elif len(x_new) == 1 and len(z_new) == 1:
            y_fst, y_snd = y_new
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_old, z_new[0]))
            new_values.append((x_rem, y_fst, z_rem))
            new_values.append((x_rem, y_snd, z_rem))
        elif len(y_new) == 1 and len(z_new) == 1:
            x_fst, x_snd = x_new
            new_values.append((x_old, y_old, z_new[0]))
            new_values.append((x_old, y_new[0], z_rem))
            new_values.append((x_fst, y_rem, z_rem))
            new_values.append((x_snd, y_rem, z_rem))
        elif len(x_new) == 1:
            y_fst, y_snd = y_new
            z_fst, z_snd = z_new
            new_values.append((x_new[0], y_old, z_old))
            new_values.append((x_rem, y_old, z_fst))
            new_values.append((x_rem, y_old, z_snd))
            new_values.append((x_rem, y_fst, z_rem))
            new_values.append((x_rem, y_snd, z_rem))
        elif len(y_new) == 1:
            x_fst, x_snd = x_new
            z_fst, z_snd = z_new
            new_values.append((x_old, y_new[0], z_old))
            new_values.append((x_fst, y_rem, z_old))
            new_values.append((x_snd, y_rem, z_old))
            new_values.append((x_rem, y_rem, z_fst))
            new_values.append((x_rem, y_rem, z_snd))
        elif len(z_new) == 1:
            x_fst, x_snd = x_new
            y_fst, y_snd = y_new
            new_values.append((x_old, y_old, z_new[0]))
            new_values.append((x_fst, y_old, z_rem))
            new_values.append((x_snd, y_old, z_rem))
            new_values.append((x_rem, y_fst, z_rem))
            new_values.append((x_rem, y_snd, z_rem))
        else:
            x_fst, x_snd = x_new
            y_fst, y_snd = y_new
            z_fst, z_snd = z_new
            new_values.append((x_fst, y_old, z_old))
            new_values.append((x_snd, y_old, z_old))
            new_values.append((x_rem, y_old, z_fst))
            new_values.append((x_rem, y_old, z_snd))
            new_values.append((x_rem, y_fst, z_rem))
            new_values.append((x_rem, y_snd, z_rem))
    return new_values

def calc_points(cuboid):
    x, y, z = cuboid
    x_range = abs(x[1]-x[0])+1
    y_range = abs(y[1]-y[0])+1
    z_range = abs(z[1]-z[0])+1
    return x_range*y_range*z_range

instrs = []
with open('input.txt') as f:
    instrs = [x.split('\n')[0].split(' ') for x in f.readlines()]

on = []
for op, value in instrs:
    x_new, y_new, z_new = [[int(y) for y in x.split('..')] for x in re.split(',?[xyz]=', value)[1:]]
    if on == [] and op == 'on':
        on.append((x_new, y_new, z_new))
    else:
        new_on = []
        for old in on:
            new_on += split(old, (x_new, y_new, z_new)) 
        on = new_on
        if op == 'on':
            on.append((x_new, y_new, z_new))

print(sum([calc_points(cub) for cub in on]))
