# https://scikit-image.org
from skimage import data, io
import numpy as np

board = data.gravel().astype(np.uint8)
# board[board == 1] = 255
board = board.tolist()

board = [[0, 255, 0, 255, 0, 255],
         [255, 0, 255, 0, 255, 0],
         [0, 255, 0, 255, 0, 255],
         [255, 0, 255, 0, 255, 0],
         [0, 255, 0, 255, 0, 255],
         [255, 0, 255, 0, 255, 0]]

io.imshow(np.array(board, dtype=np.uint8))

rows = len(board)
cols = len(board[0])

def get_value(data, r, c, offsety, offsetx):
    value = data[r][c]
    y = r + offsety
    x = c + offsetx
    # neighbors = 0.05
    neighbors = 0.1
    if y < 0 or y >= len(data):
        return value * neighbors
    if x < 0 or x >= len(data[0]):
        return value * neighbors
    if offsetx == 0 and offsety == 0:
        return value * 0.6
    value = data[y][x]
    return value * neighbors

output = []
for i in range(rows):
    inner = []
    for j in range(cols):
        c = get_value(board, i, j, 0, 0)
        c += get_value(board, i, j, -1, 0)
        c += get_value(board, i, j, 1, 0)
        c += get_value(board, i, j, 0, 1)
        c += get_value(board, i, j, 0, -1)
        inner.append(c)
    output.append(inner)

io.imshow(np.array(output, dtype=np.uint8))


# io.imshow(data.checkerboard())

data = ['Hi!']
def func(a):
    a.append('GW')
    return a

b = data
z = func(data)
z.append("?")
print("b", b)
print("data", data)
print("z", z)


data = ['Hi!']
def func(a):
    a.append('GW')
    return a

b = data
# z = 
x = func(data)
x.append("?")
print("b", b)
print("d", data)
print("z", z)


a = "hola"
def upper(cdn):
    cdn = cdn.upper()
    return cdn

b = upper(a)
print("a", a)
print("b", b)

import copy
data = ['Hi!']
def func(a):
    a.append('GW')
    return a

b = data
z = func(copy.deepcopy(data))
z.append("?")
print("b", b)
print("data", data)
print("z", z)


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

output = copy.deepcopy(data)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        tmp = output[j][i]
        output[j][i] = output[i][j]
        output[i][j] = tmp

import random
numbers = list(range(10))
random.shuffle(numbers)


numbers = [4, 8, 7, 3, 5, 9, 0, 1, 6, 2]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp

import sort
numbers = [4, 8, 7, 3, 5, 9, 0, 1, 6, 2]
sort.bubble(numbers)
print(numbers)
