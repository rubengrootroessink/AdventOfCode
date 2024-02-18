from functools import reduce

def get_sides(matrix):
    result = []
    result.append(matrix[0])
    result.append(list(reversed(matrix[0])))
    result.append(matrix[-1])
    result.append(list(reversed(matrix[-1])))
    
    side_1 = [row[0] for row in matrix]
    side_2 = [row[-1] for row in matrix]
    result.append(side_1)
    result.append(list(reversed(side_1)))
    result.append(side_2)
    result.append(list(reversed(side_2)))
    return ["".join(x) for x in result]

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    
    tiles_dict = {}

    for tile in data:
        tile_data = tile.split('\n')
        tile_num = int(tile_data[0].split(' ')[1].split(':')[0])

        tile_matrix = []
        for row in tile_data[1:]:
            tile_row = []
            for char in row:
                tile_row.append(char)
            tile_matrix.append(tile_row)
            
        if len(tile_matrix) == 11:
            tile_matrix = tile_matrix[:-1]

        tiles_dict[tile_num] = get_sides(tile_matrix)
    
    corners = []
    for key, value in tiles_dict.items():
        count = 0
        for key_2, value_2 in tiles_dict.items():
            if not key == key_2:
                for item in value:
                    if item in value_2:
                        count += 1
        
        if count // 2 == 2:
            corners.append(key)
    
    print(reduce((lambda x, y: x * y), corners))
