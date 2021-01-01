import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
bagDict = {}

for line in f:
    cleanedLine = line.replace('\n', '').replace('.', '').replace(" bags", "").replace(" bag", "")
    ruleParts = cleanedLine.split(" contain ")
    outerBag = ruleParts[0].strip()
    if (ruleParts[1] == "no other"):
        continue
    innerBags = ruleParts[1].split(", ")
    bagList = []
    for bag in innerBags:
        bagParts = bag.split(' ', 1)
        count = int(bagParts[0])
        color = bagParts[1]
        bagList.append((color, count))
    bagDict[outerBag] = bagList

total = 0
def sumBagsRecursively(outerBag):
    global total, bagDict
    if outerBag in bagDict:
        for innerBag in bagDict[outerBag]:
            total += innerBag[1]
            for _ in range(innerBag[1]):
                sumBagsRecursively(innerBag[0])
sumBagsRecursively("shiny gold")

print(f'The number of bags is {total}')