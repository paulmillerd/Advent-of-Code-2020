import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
sum = 0
yesDict = {}
groupSize = 0

def addToSumAndReset():
    global sum, yesDict, groupSize
    for k in yesDict:
        if yesDict[k] == groupSize:
            sum += 1
    groupSize = 0
    yesDict = {}

for line in f:
    if line == "\n":
        addToSumAndReset()
        continue
    groupSize += 1
    for c in line:
        if c != '\n':
            if c in yesDict:
                yesDict[c] += 1
            else:
                yesDict[c] = 1

addToSumAndReset()

print(f'The sum is {sum}')