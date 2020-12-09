import collections

def find(numbers, curr_num):  
    for integer in numbers:
        if (curr_num - integer) in numbers:
            return False
    return True
    
def find_encryption(numbers, curr_num):
    for i, integer in enumerate(numbers):
        curr_count = 0
        curr_int = i
        nr_range = []
        while curr_count < curr_num:
             curr_count += numbers[curr_int]
             nr_range.append(numbers[curr_int])
             if curr_count > curr_num:
                 break
             elif curr_count == curr_num:
                 print(min(nr_range) + max(nr_range))
             curr_int += 1

q = collections.deque([])
numbers = []
start_index = 25
with open('input.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        data = line.split('\n')[0]
        nr = int(data)
        
        if i >= start_index:
            if find(q, nr):
                find_encryption(numbers, nr)
                break
            else:
                q.popleft()
                q.append(nr)
        else:
            q.append(nr)
        numbers.append(nr)
