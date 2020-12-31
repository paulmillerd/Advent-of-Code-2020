import os, sys

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

product = 1

for slope in slopes:
    x = slope[0]
    y = slope[1]
    position = 0
    n = 0

    f = open(os.path.join(sys.path[0], "input.txt"), "r")
    a = f.read().split('\n')

    for i in range(0, len(a), y):
        stripped = a[i].strip()
        if stripped[position] == '#':
            n = n + 1
        position = (position + x) % len(stripped)

    product = product * n


print(product)