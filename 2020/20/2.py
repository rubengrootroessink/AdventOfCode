import math

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
    
def matrix_flip(matrix, d):
    matrix = [list(row) for row in matrix]
    temp_matrix = matrix.copy()
    if d=='h':
        for i in range(0,len(temp_matrix),1):
                temp_matrix[i].reverse()
    elif d=='v':
        temp_matrix.reverse()
    return(temp_matrix)
    
def matrix_rotate(matrix, turns=1):
    rotated = matrix.copy()
    for i in range(0, turns):
        rotated = list(zip(*rotated[::-1]))
    rotated = [list(x) for x in rotated]
    return rotated
    
def concat(configuration, tiles_matrices):
    result = []
    for row in configuration:
        for i in range(0, len(tiles_matrices[corners[0]])):
            result_row = []
            for column in row:
                matrix = tiles_matrices[column][i]
                result_row.append("".join(matrix))
            result.append("".join(result_row))
    return result
    
def strip(matrix):
    result = []
    for row in matrix[1:len(matrix)-1]:
        result.append(row[1:len(row)-1])
    return result
    
def orient(x, y, configuration, neighbour_dict, tiles_sides, tiles_matrices):
    start_orien = [
        ["XX", "XX", "XX"],
        ["XX", "XX", "XX"],
        ["XX", "XX", "XX"]
    ]
    
    goal_orien = [
        ["XX", "XX", "XX"],
        ["XX", "XX", "XX"],
        ["XX", "XX", "XX"]
    ]
    
    tile = configuration[x][y]
    tile_matrix = tiles_matrices[tile]
    start_orien[1][1] = tile
    goal_orien[1][1] = tile

    neighbours = neighbour_dict[tile]
    for neighbour in neighbours:
        sides = tiles_sides[neighbour]
        if "".join(tile_matrix[0]) in sides:
            start_orien[0][1] = neighbour
        elif "".join(tile_matrix[-1]) in sides:
            start_orien[2][1] = neighbour
        elif "".join([row[0] for row in tile_matrix]) in sides:
            start_orien[1][0] = neighbour
        elif "".join([row[-1] for row in tile_matrix]) in sides:
            start_orien[1][2] = neighbour

    if x != 0:
        goal_orien[0][1] = configuration[x-1][y]
    if y != 0:
        goal_orien[1][0] = configuration[x][y-1]
    if x < len(configuration[0]) - 1:
        goal_orien[2][1] = configuration[x+1][y]
    if y < len(configuration[0]) - 1:
        goal_orien[1][2] = configuration[x][y+1]
    
    curr_orien = start_orien
    for i in range(0, 4):
        curr_orien = matrix_rotate(start_orien, i)
        if curr_orien == goal_orien:
            return matrix_rotate(tile_matrix, i)
        elif matrix_flip(curr_orien, 'v') == goal_orien:
            return matrix_flip(matrix_rotate(tile_matrix, i), 'v')
        elif matrix_flip(curr_orien, 'h') == goal_orien:
            return matrix_flip(matrix_rotate(tile_matrix, i), 'h')
        elif matrix_flip(matrix_flip(curr_orien, 'v'), 'h') == goal_orien:
            return matrix_flip(matrix_flip(matrix_rotate(tile_matrix, i), 'v'), 'h')
            
def print_matrix(configuration, tiles_matrices):
    print("")
    for row in configuration:
        for i in range(0, len(tiles_matrices[corners[0]])):
            print_row = []
            for column in row:
                matrix = tiles_matrices[column][i]
                print_row.append("".join(matrix))
            print(" ".join(print_row))
        print("")

def check_sea_monster(concatted_matrix, sea_monster, x, y, len_sea_monster):
    count = 0
    for i, row in enumerate(sea_monster):
        for j, column in enumerate(row):
            if column == "#":
                if concatted_matrix[x+i][y+j] == "#":
                    count += 1
    return count == len_sea_monster
    
def replace_sea_monster(matrix, sea_monster, x, y, len_sea_monster):
    matrix = [list(row) for row in matrix]
    count = 0
    for i, row in enumerate(sea_monster):
        for j, column in enumerate(row):
            if column == "#":
                matrix[x+i][y+j] = "O"
    matrix = ["".join(row) for row in matrix]
    return matrix
    
def sea_monster_check(concatted_matrix):    
    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    len_sea_monster = 15
    
    row_length = len(concatted_matrix[0])
    count = 0
    for i in range(0, len(concatted_matrix)-2):
        for j in range(0, row_length - len(sea_monster[0])):
            if check_sea_monster(concatted_matrix, sea_monster, i, j, len_sea_monster):
                count += 1
    return count > 0
    
def sea_monster_replace(concatted_matrix):    
    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    len_sea_monster = 15
    
    result_matrix = concatted_matrix.copy()
    
    row_length = len(concatted_matrix[0])
    count = 0
    for i in range(0, len(concatted_matrix)-2):
        for j in range(0, row_length - len(sea_monster[0])):
            if check_sea_monster(concatted_matrix, sea_monster, i, j, len_sea_monster):
                result_matrix = replace_sea_monster(result_matrix, sea_monster, i, j, len_sea_monster)
                
    return result_matrix
    
def find_right_orientation(matrix):
    for i in range(0, 4):
        concatted_matrix = matrix.copy()
        concatted_matrix = matrix_rotate(concatted_matrix, i)
        concatted_matrix = ["".join(row) for row in concatted_matrix]
        if sea_monster_check(concatted_matrix):
            return concatted_matrix
        elif sea_monster_check(matrix_flip(concatted_matrix, 'v')):
            concatted_matrix = matrix_flip(concatted_matrix, 'v')
            concatted_matrix = ["".join(row) for row in concatted_matrix]
            return concatted_matrix
        elif sea_monster_check(matrix_flip(concatted_matrix, 'h')):
            concatted_matrix = matrix_flip(concatted_matrix, 'h')
            concatted_matrix = ["".join(row) for row in concatted_matrix]
            return concatted_matrix
        elif sea_monster_check(matrix_flip(matrix_flip(concatted_matrix, 'v'), 'h')):
            concatted_matrix = matrix_flip(matrix_flip(concatted_matrix, 'v'), 'h')
            concatted_matrix = ["".join(row) for row in concatted_matrix]
            return concatted_matrix

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    
    tiles_sides = {}
    tiles_matrices = {}
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

        tiles_sides[tile_num] = get_sides(tile_matrix)
        tiles_matrices[tile_num] = tile_matrix
    
    corners = []
    neighbour_dict = {}
    for key, value in tiles_sides.items():
        neighbours = []
        for key_2, value_2 in tiles_sides.items():
            if not key == key_2:
                for item in value:
                    if item in value_2:
                        neighbours.append(key_2)
                        
        neighbour_dict[key] = list(set(neighbours))
        if len(neighbour_dict[key]) == 2:
            corners.append(key)
        
    configuration = []
    for x in range(0, int(math.sqrt(len(tiles_sides)))):
        row = []
        for y in range(0, int(math.sqrt(len(tiles_sides)))):
            row.append([])
        configuration.append(row)
    
    start_corner = corners[0]
    neighbours = neighbour_dict[start_corner]
    configuration[0][0] = start_corner
    configuration[0][1] = neighbours[0]
    configuration[1][0] = neighbours[1]
    configuration[1][1] = [x for x in list(set(neighbour_dict[neighbours[0]]).intersection(set(neighbour_dict[neighbours[1]]))) if x != start_corner][0]
    
    count = 0
    already_placed = [configuration[0][0], configuration[0][1], configuration[1][0], configuration[1][1]]
    while any([True for x in configuration if [] in x]) and count != 1:
        for x, row in enumerate(configuration):
            for y, column in enumerate(row):
                if configuration[x][y] == []:
                    if x == 0:
                        a = configuration[x][y-1]
                        b = configuration[x+1][y-1]
                        if a != []:
                            if b != []:
                                for a_n in neighbour_dict[a]:
                                    for b_n in neighbour_dict[b]:
                                        if a_n in neighbour_dict[b_n] and b_n in neighbour_dict[a_n] and not a_n in already_placed and not b_n in already_placed:
                                            configuration[x][y] = a_n
                                            already_placed.append(a_n)
                                            configuration[x+1][y] = b_n
                                            already_placed.append(b_n)
                    if y == 0:
                        a = configuration[x-1][y]
                        b = configuration[x-1][y+1]
                        if a != []:
                            if b != []:
                                for a_n in neighbour_dict[a]:
                                    for b_n in neighbour_dict[b]:
                                        if a_n in neighbour_dict[b_n] and b_n in neighbour_dict[a_n] and not a_n in already_placed and not b_n in already_placed:
                                            configuration[x][y] = a_n
                                            already_placed.append(a_n)
                                            configuration[x][y+1] = b_n
                                            already_placed.append(b_n)
                    elif configuration[x-1][y] != [] and configuration[x][y-1] != []:
                        a = configuration[x-1][y]
                        b = configuration[x][y-1]
                        configuration[x][y] = [z for z in list(set(neighbour_dict[a]).intersection(set(neighbour_dict[b]))) if not z in already_placed][0]
                        already_placed.append(configuration[x][y])
                    elif configuration[x][y] != []:
                        pass
                    elif configuration[x][y] != []:
                        pass
        count = 1
    
    for x, row in enumerate(configuration):
        for y, column in enumerate(row):
            tiles_matrices[column] = orient(x, y, configuration, neighbour_dict, tiles_sides, tiles_matrices)
            
    #print_matrix(configuration, tiles_matrices)
            
    for x, row in enumerate(configuration):
        for y, column in enumerate(row):
            tiles_matrices[column] = strip(tiles_matrices[column])
    
    concatted_matrix = concat(configuration, tiles_matrices)
    matrix = find_right_orientation(concatted_matrix)

    matrix = sea_monster_replace(matrix)

    count = 0
    for row in matrix:
        for column in row:
            if column == "#":
                count += 1
    print(count)
