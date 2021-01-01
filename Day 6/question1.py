import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
sum = 0
yesQuestions = set()

def addToSumAndReset():
    global sum, yesQuestions
    sum += len(yesQuestions)
    yesQuestions = set()

for line in f:
    if line == "\n":
        addToSumAndReset()
        continue
    for c in line:
        if c != '\n':
            yesQuestions.add(c)

addToSumAndReset()

print(f'The sum is {sum}')