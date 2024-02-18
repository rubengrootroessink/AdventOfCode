def find_split(mirror):

    # Try each split
    for i in range(1, len(mirror)):
        left = mirror[:i]
        right = mirror[i:]

        trim = min(len(left), len(right))
       
        left = left[-trim:]
        right = list(reversed(right[:trim]))

        diff_count = 0
        for j in range(trim):
            for k in range(len(left[0])):
                if left[j][k] != right[j][k]:
                    diff_count += 1

        if diff_count == 1:
            return i

    return 0

with open('input.txt') as f:
    mirrors = [x.split('\n') for x in f.read()[:-1].split('\n\n')]
    mirrors = [[''.join(['1' if y == '#' else '0' for y in x]) for x in mirror] for mirror in mirrors]

result = 0
for mirror in mirrors:
    h_result = find_split(mirror)
    v_result = find_split(list(map(''.join, zip(*mirror))))
    result += 100*h_result + v_result

print(result)
