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
    reindeer_scores = {}
    for i in range(1, total_time+1):
        furthest_dist = 0
        furthest_reindeers = []
        for key, value in reindeers.items():
            wave_time = value['fly_time'] + value['rest_time']
            kms = math.floor(i / wave_time) * value['speed'] * value['fly_time']
            rest_time = min(i % wave_time, value['fly_time'])
            kms += rest_time * value['speed']
        
            if kms > furthest_dist:
                furthest_dist = kms
                furthest_reindeers = [key]
            elif kms == furthest_dist:
                furthest_dist = kms
                furthest_reindeers.append(key)
            
        for furthest_reindeer in furthest_reindeers:
            if furthest_reindeer in reindeer_scores.keys():
                reindeer_scores[furthest_reindeer] += 1
            else:
                reindeer_scores[furthest_reindeer] = 1

    print(max(reindeer_scores.items(), key=lambda x: x[1])[1])
