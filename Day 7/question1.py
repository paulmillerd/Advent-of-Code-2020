import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
bagDict = {}

for line in f:
    cleanedLine = line.replace('\n', '').replace('.', '').replace(" bags", "").replace( "bag", "")
    ruleParts = cleanedLine.split(" contain ")
    outerBag = ruleParts[0].strip()
    if (ruleParts[1] == "no other"):
        continue
    innerBags = ruleParts[1].split(", ")
    for bag in innerBags:
        color = bag.split(' ', 1)[1].strip()
        if color in bagDict:
            bagDict[color].add(outerBag)
        else:
            bagDict[color] = {outerBag}

bagSet = set()
def addBagsRecursively(innerBag):
    global bagSet, bagDict
    if innerBag in bagDict:
        for outerBag in bagDict[innerBag]:
            bagSet.add(outerBag)
            addBagsRecursively(outerBag)
addBagsRecursively("shiny gold")

print(f'The number of bags is {len(bagSet)}')