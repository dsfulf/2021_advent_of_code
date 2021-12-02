with open('input.txt', 'r') as f:
    data = [int(i.strip()) for i in f.readlines()]

# part 1

count = 0
for cur, nex in zip(data, data[1:]):
    if nex > cur:
        count += 1
print(count)


# part 2

import numpy as np

kernel = [1.0 / 3.0] * 3
mvg = np.round(np.convolve(data, kernel, mode='valid'), 10)

count = 0
for cur, nex in zip(mvg, mvg[1:]):
    if nex > cur:
        count += 1
print(count)
