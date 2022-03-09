inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()

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

gammaResult = [0] * binaryLength
epsilonResult = [0] * binaryLength

epsilonRate = ""
gammaRate = ""

print(f"{oneCounter}, {zeroCounter}")
for i in range(len(gammaResult)):
    if oneCounter[i] > zeroCounter[i]:
        gammaResult[i] = 1
    elif zeroCounter[i] > oneCounter[i]:
        gammaResult[i] = 0

    gammaRate = f"{gammaRate}{gammaResult[i]}"

print(gammaRate)

for i in range(len(epsilonResult)):
    if oneCounter[i] > zeroCounter[i]:
        epsilonResult[i] = 0
    elif zeroCounter[i] > oneCounter[i]:
        epsilonResult[i] = 1

    epsilonRate = f"{epsilonRate}{epsilonResult[i]}"

print(epsilonRate)

print(f"Power consumption is at {int(gammaRate, 2) * int(epsilonRate,2)}")