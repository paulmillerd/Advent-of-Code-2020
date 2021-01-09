import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")

instructions = []
for line in f:
    instructions.append([line.replace('\n', '').strip(), False])

acc = 0
i = 0
while not instructions[i][1]:
    nextStepDistance = 1
    parts = instructions[i][0].split(' ')
    operation = parts[0]
    argument = parts[1]
    if operation == 'acc':
        acc += int(argument)
    elif operation == 'jmp':
        nextStepDistance = int(argument)
    instructions[i][1] = True
    i += nextStepDistance

print(f'acc = {acc}')