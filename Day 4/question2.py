import os, sys

f = open(os.path.join(sys.path[0], "input.txt"), "r")
emptyLine = "\n"
requiredFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
validCount = 0
foundFields = set()

decDigits = "0123456789"
hexDigits = decDigits + "abcdef"
eyeColors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def checkValidity():
    global validCount, foundFields
    if len(foundFields) == len(requiredFields):
        validCount += 1
    foundFields = set()

def validateNumber(value, start, end):
    try:
        intValue = int(value)
        return start <= intValue <= end
    except ValueError:
        return False

def validateField(name, value):
    if name == "byr":
        return validateNumber(value, 1920, 2002)
    elif name == "iyr":
        return validateNumber(value, 2010, 2020)
    elif name == "eyr":
        return validateNumber(value, 2020, 2030)
    elif name == "hgt":
        unit = value[-2:]
        if unit == "cm":
            return validateNumber(value[:-2], 150, 193)
        elif unit == "in":
            return validateNumber(value[:-2], 59, 76)
        else:
            return False
    elif name == "hcl":
        global hexDigits
        return value[:1] == '#' and all(c in hexDigits for c in value[1:])
    elif name == "ecl":
        global eyeColors
        return value in eyeColors
    elif name == "pid":
        global decDigits
        return len(value) == 9 and all(c in decDigits for c in value)
    else:
        return False

for line in f:
    if line == emptyLine:
        checkValidity()
    else:
        fields = line.split(' ')
        for field in fields:
            fieldParts = field.split(':')
            if len(fieldParts) > 2:
                continue
            fieldName = fieldParts[0]
            fieldValue = fieldParts[1].replace('\n', '')
            if fieldName in requiredFields and fieldName not in foundFields and validateField(fieldName, fieldValue):
                foundFields.add(fieldName)

checkValidity()

print(f'Number of valid passports: {validCount}')