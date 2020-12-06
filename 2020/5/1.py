def binary_split(item_string, max):
    seat_nums = list(range(0, max + 1))
    for char in item_string:
        if char in 'FL':
            seat_nums = seat_nums[:len(seat_nums)//2]
        elif char in 'BR':
            seat_nums = seat_nums[len(seat_nums)//2:]
    return seat_nums[0]

def calc_seat(seat_string):
    row_string, column_string = seat_string[0:7], seat_string[7:10]
    row = binary_split(row_string, 127)
    column = binary_split(column_string, 7)
    return row * 8 + column

def test_case():
    print(calc_seat('FBFBBFFRLR'))
    print(calc_seat('BFFFBBFRRR'))
    print(calc_seat('FFFBBBFRRR'))
    print(calc_seat('BBFFBBFRLL'))
    
#test_case()

seat_nums = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        data = line.split('\n')[0]
        seat = calc_seat(data)
        seat_nums.append(seat)
    
print(max(seat_nums))
