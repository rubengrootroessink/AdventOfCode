import math

with open('input.txt', 'r') as f:
    reindeers = {}
    for data in f.readlines():
        line = data.split('\n')[0].split(' ')
        reindeer = line[0]
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[-2])
        reindeers[reindeer] = {'speed': speed, 'fly_time': fly_time, 'rest_time': rest_time}
        
    total_time = 2503
    furthest_dist = 0
    furthest_reindeer = ''
    for key, value in reindeers.items():
        wave_time = value['fly_time'] + value['rest_time']
        kms = math.floor(total_time / wave_time) * value['speed'] * value['fly_time']
        rest_time = min(total_time % wave_time, value['fly_time'])
        kms += rest_time * value['speed']
        
        if kms > furthest_dist:
            furthest_dist = kms
            furthest_reindeer = key
            
    print(furthest_dist)
