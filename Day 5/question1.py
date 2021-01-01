import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
highestSeatId = 0

def narrowDownRecursively(str, min, max):
    if len(str) == 0:
        return max
    c = str[0]
    if c == 'F' or c == 'L':
        newMax = max - int((max - min + 1) / 2)
        return narrowDownRecursively(str[1:], min, newMax)
    else:
        newMin = min + int((max - min + 1) / 2)
        return narrowDownRecursively(str[1:], newMin, max)

for line in f:
    row = narrowDownRecursively(line[:7], 0, 127)
    column = narrowDownRecursively(line[7:10], 0, 7)
    seatId = row * 8 + column
    if seatId > highestSeatId:
        highestSeatId = seatId

print(f'Highest seat ID: {highestSeatId}')