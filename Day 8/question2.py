import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")

instructions = []
for line in f:
    instructions.append([line.replace('\n', '').strip(), False])

jmpsIgnored = set()
acc = 0
while not instructions[len(instructions) - 1][1]:
    for instruction in instructions:
        instruction[1] = False

    jmpIgnored = False
    acc = 0
    i = 0
    while i < len(instructions) and not instructions[i][1]:
        nextStepDistance = 1
        parts = instructions[i][0].split(' ')
        operation = parts[0]
        argument = parts[1]
        if operation == 'acc':
            acc += int(argument)
        elif operation == 'jmp':
            if not jmpIgnored and i not in jmpsIgnored:
                jmpsIgnored.add(i)
                jmpIgnored = True
            else:
                nextStepDistance = int(argument)
        instructions[i][1] = True
        i += nextStepDistance

print(f'acc = {acc}')