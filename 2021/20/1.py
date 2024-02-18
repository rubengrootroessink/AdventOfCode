import copy

image = {}
algo = []
with open('input.txt') as f:
    data = f.read().split('\n\n')
    algo = data[0].strip()
    image_data = [x.strip() for x in data[1].split('\n') if x != '']
    for j, row in enumerate(image_data):
        for i, column in enumerate(row):
            image[(j,i)] = column

def find_square(y, x):
    return [
        (y-1, x-1), (y-1, x), (y-1, x+1),
        (y, x-1),   (y, x),   (y, x+1),
        (y+1, x-1), (y+1, x), (y+1, x+1),
    ]

def find_affected(image):
    affected = set()
    for y, x in image:
        for pixel in find_square(y, x):
            affected.add(pixel)
    return affected

def check_pixel(pixel, image, algo, count=1):
    y, x = pixel
    
    square = find_square(y, x)
    
    result = ''
    for item in square:
        if item in image.keys():
            result += '1' if image[item] == '#' else '0'
        else:
            if algo[0] == '#' and algo[-1] == '.':
                result += '0' if count == 1 else '1'
            else:
                result += '0'
    return algo[int(result, 2)] == '#'

def enhance(image, algo, count=1):
    new_image = {}
    affected = find_affected(image)
    for pixel in affected:
        new_image[pixel] = '#' if check_pixel(pixel, image, algo, count) else 0
    return new_image

for i in range(0, 2):
    image = enhance(image, algo, count=i%2+1)
print(len([k for k, v in image.items() if v == '#']))
