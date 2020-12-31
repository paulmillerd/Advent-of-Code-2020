import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")

movement = 3
position = 0
n = 0

for line in f:
    stripped = line.strip()
    if stripped[position] == '#':
        n = n + 1
    position = (position + movement) % len(stripped)


print(n)