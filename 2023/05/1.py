def input_helper(input_var):
    result = []
    for rng in input_var:
        dst, src, length = [int(x) for x in rng.split()]
        result.append((range(src, src+length), range(dst, dst+length)))
    return result

def transfer(input_vars, selected_map):
    return_vars = []
    for input_var in input_vars:
        return_var = None
        for src_rng, dst_rng in selected_map:
            if input_var in src_rng:
                return_var = dst_rng[0]+(input_var-src_rng[0])
                break
        return_vars.append(input_var if return_var == None else return_var)

    return return_vars

with open('input.txt') as f:
    data = f.read()[:-1].split('\n\n')

seeds, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = [x.split('\n')[1:] if i != 0 else x for i, x in enumerate(data)]

seeds = [int(x) for x in seeds.split(' ') if x.isdigit()]
seed_soil = input_helper(seed_soil)
soil_fert = input_helper(soil_fert)
fert_water = input_helper(fert_water)
water_light = input_helper(water_light)
light_temp = input_helper(light_temp)
temp_humid = input_helper(temp_humid)
humid_loc = input_helper(humid_loc)

full_data = [seeds]

full_data.append(transfer(full_data[-1], seed_soil))
full_data.append(transfer(full_data[-1], soil_fert))
full_data.append(transfer(full_data[-1], fert_water))
full_data.append(transfer(full_data[-1], water_light))
full_data.append(transfer(full_data[-1], light_temp))
full_data.append(transfer(full_data[-1], temp_humid))
full_data.append(transfer(full_data[-1], humid_loc))

print(min(full_data[-1]))
