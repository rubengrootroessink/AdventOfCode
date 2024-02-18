def gen_sk(pk, lps):
    curr_val = 1
    for i in range(0, lps):
        curr_val = (curr_val * pk) % 20201227
    return curr_val

def find_loop_size(pk):
    curr_val = 1
    nr_loops = 0
    while curr_val != pk:
        curr_val = (curr_val * 7) % 20201227
        nr_loops += 1
    return nr_loops
        
with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    pk_card = int(data[0])
    pk_door = int(data[1])
    
    lps_card = find_loop_size(pk_card)    
    lps_door = find_loop_size(pk_door)

    result = gen_sk(pk_card, lps_door)
    print(result)
