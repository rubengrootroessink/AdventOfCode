import collections

def find(numbers, curr_num):  
    for integer in numbers:
        if (curr_num - integer) in numbers:
            return False
    return True

q = collections.deque([])
start_index = 25
with open('input.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        data = line.split('\n')[0]
        nr = int(data)
        
        if i >= start_index:
            if find(q, nr):
                print(nr)
                break
            else:
                q.popleft()
                q.append(nr)
        else:
            q.append(nr)
