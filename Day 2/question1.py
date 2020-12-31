import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")

n = 0
for line in f:
    inputs = line.split(':', 2)
    password = inputs[1].strip()
    ruleParts = inputs[0].split(' ', 2)
    letter = ruleParts[1]
    ruleCounts = ruleParts[0].split('-', 2)
    minimum = int(ruleCounts[0])
    maximum = int(ruleCounts[1])
    count = password.count(letter)
    if minimum <= count and count <= maximum:
        n = n + 1

print(f'Number of valid passwords: {n}')