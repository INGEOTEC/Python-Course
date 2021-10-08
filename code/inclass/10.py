# https://scikit-image.org
from skimage import data, io
import numpy as np

image = data.coins()

# io.imshow(image)

lst = image.tolist()

print(len(lst), len(lst[0]))

rows = []

r = 0
c = 0
for i in lst:
    c = 0
    row = []
    for j in i:
        # print(r , c, "value", j)
        if c > 150:
            v = 255 - j
        else:
            v = j
        row.append(v)
        c += 1
    r += 1
    rows.append(row)


n = np.array(rows, dtype=np.uint8)
io.imshow(n)

im = [[2, 3, 4],[234, 100, 123]]
n = np.array(im, dtype=np.uint8)
io.imshow(n)
