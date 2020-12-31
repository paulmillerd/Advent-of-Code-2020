import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
target = 2020
numbers = set()

for line in f:
    numbers.add(int(line))

for number1 in numbers:
    diff1 = target - number1
    for number2 in numbers:
        if number1 == number2:
            continue
        diff2 = diff1 - number2
        if diff2 in numbers:
            print (f'{number1} * {number2} * {diff2} = {number1*number2*diff2}')
            exit()