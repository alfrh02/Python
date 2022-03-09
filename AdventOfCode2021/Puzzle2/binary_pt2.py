inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()
fileLinesOriginal = fileLines

binaryLength = len(fileLines[0]) - 1

zeroCounter = [0] * binaryLength
oneCounter = [0] * binaryLength

x = 0
def count():
    for i in range(len(fileLines)):
        letter = fileLines[i]

        if letter[x] == "0":
            zeroCounter[x] += 1
        elif letter[x] == "1":
            oneCounter[x] += 1

while True:
    count()
    x += 1
    if x == binaryLength:
        break

horizontal = [0] * binaryLength
horizontal_invert = [0] * binaryLength

inputFile.close()

for i in range(len(horizontal)):
    if oneCounter[i] > zeroCounter[i]:
        horizontal[i] = 1
        horizontal_invert[i] = 0
    elif zeroCounter[i] > oneCounter[i]:
        horizontal[i] = 0
        horizontal_invert[i] = 1

def parse(max, average):
    global fileLines, fileLinesOriginal

    letters = range(0,max)
    for letter in letters:
        inputFile = open("input.txt", "w")
        for line in fileLinesOriginal:
            if line[letter] == str(average[letter]):
                inputFile.write(line)
        inputFile.close()
        inputFile = open("input.txt", "r")
        fileLines = inputFile.readlines()

    inputFile.close()
    inputFile = open("input.txt", "w")
    for line in fileLinesOriginal:
        inputFile.write(line)

    return fileLines[0]

inputFile.close()

oxygenResult = parse(11, horizontal)
CO2result = parse(11, horizontal_invert)

print(f"Oxygen generator rating: {oxygenResult}, or {int(oxygenResult,2)} in decimal.")
print(f"CO2 scrubber rating: {CO2result}, or {int(CO2result,2)} in decimal.")

print(f"Overall life support rating: {int(oxygenResult,2) * int(CO2result,2)}")