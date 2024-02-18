def input_helper(input_var):
    result = []
    for rng in input_var:
        dst, src, length = [int(x) for x in rng.split()]
        result.append((range(src, src+length), range(dst, dst+length)))
    return result

def find_source_slices(input_slice, selected_map):
    src_slices = []
    found = False
    
    for src_rng, dst_rng in selected_map:
        if input_slice[0] in range(src_rng[0], src_rng[-1]+1) and input_slice[-1] in range(src_rng[0], src_rng[-1]+1):
            src_slices.append(input_slice)
            found = True
        elif input_slice[0] < src_rng[0] and input_slice[-1] in range(src_rng[0], src_rng[-1]+1):
            left_range = range(input_slice[0], src_rng[0])
            f, sub_slices = find_source_slices(left_range, selected_map)
            if not f:
                src_slices.append(left_range)
            else:
                src_slices = src_slices + sub_slices 

            src_slices.append(range(src_rng[0], input_slice[-1]+1))
            found = True
        elif input_slice[0] in range(src_rng[0], src_rng[-1]+1) and input_slice[-1] >= src_rng[-1]+1:
            src_slices.append(range(input_slice[0], src_rng[-1]+1))

            right_range = range(src_rng[-1]+1, input_slice[-1]+1)
            f, sub_slices = find_source_slices(right_range, selected_map)
            if not f:
                src_slices.append(right_range)
            else:
                src_slices = src_slices + sub_slices
            
            found = True
        elif input_slice[0] < src_rng[0] and input_slice[-1] >= src_rng[-1]:
            src_slices.append(range(src_rng[0], src_rng[-1]+1))

            left_range = range(input_slice[0], src_rng[0])
            f, sub_slices = find_source_slices(left_range, selected_map)
            if not f:
                src_slices.append(left_range)
            else:
                src_slices = src_slices + sub_slices

            right_range = range(src_rng[-1]+1, input_slice[-1]+1)
            f, sub_slices = find_source_slices(right_range, selected_map)
            if not f:
                src_slices.append(right_range)
            else:
                src_slices = src_slices + sub_slices
            
            found = True
    return found, src_slices

def transfer(input_vars, selected_map):
    return_vars = []
    for input_var in input_vars:
        found, src_slices = find_source_slices(input_var, selected_map)

        result_slices = []
        if not found:
            result_slices.append(input_var)
        
        src_slices = list(set(src_slices))
        for sliced in src_slices:
            found = False
            for src_rng, dst_rng in selected_map:
                if sliced[0] in src_rng:
                    result_slices.append(range((sliced[0]-src_rng[0])+dst_rng[0], ((sliced[-1]+1)-src_rng[0])+dst_rng[0]))
                    found = True
            if not found:
                result_slices.append(sliced)

        return_vars = return_vars + result_slices if result_slices != [] else return_vars

    return return_vars

with open('input.txt') as f:
    data = f.read()[:-1].split('\n\n')

seeds, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc = [x.split('\n')[1:] if i != 0 else x for i, x in enumerate(data)]

seeds = [int(x) for x in seeds.split(' ') if x.isdigit()]
seeds = [range(seeds[i*2], seeds[i*2]+seeds[(i*2)+1]) for i in range(len(seeds)//2)]

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

print(min([x[0] for x in full_data[-1]]))
