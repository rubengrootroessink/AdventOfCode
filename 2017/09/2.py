import re

with open('input.txt') as f:
    streams = [x.split('\n')[0] for x in f.readlines()]

for stream in streams:
    clean_stream = re.sub('!.', '', stream)
    garbage = re.findall('<.*?>', clean_stream)
    print(sum([len(x)-2 for x in garbage]))
