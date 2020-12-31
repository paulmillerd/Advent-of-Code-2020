import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
target = 2020
numbers = set()

for line in f:
    numbers.add(int(line))

for number in numbers:
    diff = target - number
    if diff in numbers:
        print(f'{number} * {diff} = {number*diff}')
        break