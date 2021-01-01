import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
emptyLine = "\n"
requiredFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
validCount = 0
foundFields = set()

def checkValidity():
    global validCount, foundFields
    if len(foundFields) == len(requiredFields):
        validCount += 1
    foundFields = set()

for line in f:
    if line == emptyLine:
        checkValidity()
    else:
        fields = line.split(' ')
        for field in fields:
            fieldName = field.split(':')[0]
            if fieldName in requiredFields:
                foundFields.add(fieldName)

checkValidity()

print(f'Number of valid passports: {validCount}')