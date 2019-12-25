import sys
input = open("day8/input.txt").read()

def build_layers(data):
    layers, n = [], width * height
    for i in range(len(data) // n):
        layers.append([list(map(int, data[i*n + j*width : i*n + (j+1)*width])) for j in range(height)])
    return layers

def count_pixels(image, x):
    return sum(1 for row in image for col in row if col == x)

width, height = 25, 6
layers = build_layers(input)

_, layer = min((count_pixels(layer, 0), layer) for layer in layers)
print("Part 1: "+str(count_pixels(layer, 1) * count_pixels(layer, 2)))

image = [['#']*width for _ in range(height)]
for r in range(height):
    for c in range(width):
        pixel = next(layer[r][c] for layer in layers if layer[r][c] != 2)
        image[r][c] = '*' if pixel == 1 else ' '
print("Part 2:\n"+'\n'.join(''.join(row) for row in image))